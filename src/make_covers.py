"""Render blog cover images (1200x630 JPG) with headless Chrome. Run from src/: py make_covers.py
Output goes to src/blog-img/, which build.py copies to /blog/img/. Uses the real logo file, brand fonts and colours."""
import html, os, subprocess, sys, tempfile
from posts import POSTS

CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
HB = "M927 298 1200 25 590 25 117 498 294.5 473 394.5 373Z"
HR = "M1158 218 1001.5 240 921.5 320 452 386 227 611 765 611Z"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "blog-img")
os.makedirs(OUT, exist_ok=True)
browser = next(p for p in CHROME if os.path.exists(p))

TEMPLATE = """<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:B;src:url(../fonts/bricolage.woff2);font-weight:200 800}}
@font-face{{font-family:J;src:url(../fonts/jakarta.woff2);font-weight:200 800}}
*{{box-sizing:border-box}}html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#fff;color:#0D0D0D}}body{{position:relative}}
.logo{{position:absolute;left:64px;top:52px;width:230px}}
.hands{{position:absolute;right:-170px;top:-30px;width:560px}}
.k{{position:absolute;left:64px;top:224px;font:700 26px/1 J;color:#1A6FC2}}
h1{{position:absolute;left:64px;top:268px;width:810px;margin:0;font:700 74px/1.02 B;letter-spacing:-.03em}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:84px;background:#0D0D0D;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 64px;font:600 25px/1 J}}
.bar b{{font:700 40px/1 B;letter-spacing:-.01em}}
{extra}</style>{logo}
<svg class="hands" viewBox="100 10 1080 615"><path fill="#4BA4F4" d="{hb}"/><path fill="#E73A2A" d="{hr}"/></svg>
<div class="k">{cat}</div><h1>{cover}</h1>
{bar}"""

# Social image: full lockup. Card image: shown small on the site, so no logo (brand minimum is 160 px wide).
VARIANTS = {
    "": dict(extra="", logo='<img class="logo" src="../logo.svg" alt="">',
             bar='<div class="bar"><span>Call / WhatsApp</span><b>75609 21593</b></div>'),
    "-card": dict(extra=".k{{top:236px;font-size:36px}}h1{{top:292px;width:1040px;font-size:104px}}.hands{{right:-120px;top:-70px;width:520px}}".replace("{{", "{").replace("}}", "}"),
                  logo="", bar=""),
}


def to_jpg(png, jpg):
    try:
        from PIL import Image
        Image.open(png).convert("RGB").crop((0, 0, 1200, 630)).save(jpg, quality=86, optimize=True, progressive=True)
    except ImportError:
        ps = ("Add-Type -AssemblyName System.Drawing;"
              f"$s=[Drawing.Bitmap]::FromFile('{png}');$d=New-Object Drawing.Bitmap 1200,630;"
              "$g=[Drawing.Graphics]::FromImage($d);$g.DrawImage($s,0,0,(New-Object Drawing.Rectangle 0,0,1200,630),[Drawing.GraphicsUnit]::Pixel);"
              "$c=[Drawing.Imaging.ImageCodecInfo]::GetImageEncoders()|?{$_.MimeType -eq 'image/jpeg'};"
              "$e=New-Object Drawing.Imaging.EncoderParameters 1;$e.Param[0]=New-Object Drawing.Imaging.EncoderParameter ([Drawing.Imaging.Encoder]::Quality),86L;"
              f"$d.Save('{jpg}',$c,$e);$g.Dispose();$d.Dispose();$s.Dispose()")
        subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=True)


with tempfile.TemporaryDirectory() as tmp:
    for p, suffix in [(p, s) for p in POSTS for s in VARIANTS]:
        page = os.path.join(HERE, "_cover.html")
        with open(page, "w", encoding="utf-8") as f:
            f.write(TEMPLATE.format(hb=HB, hr=HR, cat=html.escape(p["cat"]), cover=html.escape(p["cover"]), **VARIANTS[suffix]))
        png = os.path.join(tmp, p["slug"] + suffix + ".png")
        subprocess.run([browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                        "--allow-file-access-from-files", f"--user-data-dir={os.path.join(tmp, 'profile')}",
                        "--virtual-time-budget=3000", "--window-size=1200,760", f"--screenshot={png}",
                        "file:///" + page.replace("\\", "/")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
        to_jpg(png, os.path.join(OUT, p["slug"] + suffix + ".jpg"))
        os.remove(page)
        print("cover", p["slug"] + suffix)
sys.exit(0)
