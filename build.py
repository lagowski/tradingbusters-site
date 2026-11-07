"""Genera las páginas estáticas con una cabecera y un pie comunes. Uso: python3 build.py (sin dependencias, sin rastreadores)."""

from pathlib import Path

EMAIL = "ainews402@gmail.com"
UPDATED = "7 de noviembre de 2026"
BRAND = "Trading Busters"
ROOT = Path(__file__).parent

PROFILES = [
    ("YouTube @tradingbustersoficial", "https://www.youtube.com/@tradingbustersoficial"),
    ("TikTok @tradingbustersoficial", "https://www.tiktok.com/@tradingbustersoficial"),
    ("Instagram @tradingbustersoficial", "https://www.instagram.com/tradingbustersoficial/"),
]


def page(path: str, title: str, description: str, body: str, robots: str = "") -> None:
    up = "../" if path else ""
    mail = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{description}">{robots}
<link rel="icon" href="{up}favicon.png"><link rel="stylesheet" href="{up}style.css"></head><body><div class="wrap">
<header><a class="brand" href="{up or './'}">{BRAND}</a>
<nav><a href="{up or './'}">Inicio</a><a href="{up}privacy/">Privacidad</a><a href="{up}terms/">Condiciones</a></nav></header>
{body.replace("{MAIL}", mail).replace("{UPDATED}", UPDATED).replace("{UP}", up)}
<footer><a href="{up or './'}">Inicio</a><a href="{up}privacy/">Política de privacidad</a><a href="{up}terms/">Condiciones de uso</a><br>
&copy; 2026 {BRAND} &middot; Contacto: {mail}</footer></div></body></html>
"""
    out = ROOT / path / "index.html" if path else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


follow = " &middot; ".join(f'<a href="{u}">{n}</a>' for n, u in PROFILES)

page("", "Trading Busters: estrategias de trading puestas a prueba",
     "Vídeos cortos que prueban con datos las estrategias de trading que se venden en redes. No vendemos nada.", f"""
<h1>Estrategias de trading, puestas a prueba con datos.</h1>
<p class="lead">Trading Busters hace vídeos cortos en español que cogen las estrategias de trading que circulan en redes,
las convierten en una regla exacta, las prueban con datos reales y cuentan el resultado. No vendemos cursos, señales ni
nada. Nuestros vídeos son informativos y no son consejo de inversión.</p>
<div class="card"><h2>Qué hace la app Trading Busters Publisher</h2>
<p>Trading Busters Publisher es una herramienta interna que usa solo el equipo de Trading Busters. Sirve para:</p>
<ul><li>subir nuestros propios vídeos terminados, con su título y descripción, a nuestro canal de YouTube y a nuestras
cuentas de TikTok, Instagram y Facebook;</li>
<li>leer la información básica de nuestras propias cuentas y las estadísticas de nuestros propios vídeos (visualizaciones
y número de seguidores), para comprobar que las subidas funcionan y saber qué vídeos le resultan útiles a la gente.</li></ul>
<p>La app no ofrece cuentas al público y no accede a datos de nadie más. Cada publicación la aprueba antes una persona.</p></div>
<div class="card"><h2>Síguenos</h2><p>{follow}</p></div>
<div class="card yt"><picture><source srcset="assets/developed-with-youtube-light-text.png" media="(prefers-color-scheme: dark)">
<img src="assets/developed-with-youtube-dark-text.png" alt="Developed with YouTube" width="300" height="107"></picture>
<p>Trading Busters Publisher usa los <a href="https://developers.google.com/youtube/terms/api-services-terms-of-service">servicios
de la API de YouTube</a>. Lee cómo trata los datos en nuestra <a href="privacy/#youtube">política de privacidad</a> y las
<a href="https://www.youtube.com/t/terms">condiciones de servicio de YouTube</a>.</p></div>
<p>Lee nuestra <a href="privacy/">política de privacidad</a> y nuestras <a href="terms/">condiciones de uso</a>. Preguntas: {{MAIL}}.</p>
""")

page("privacy", "Política de privacidad - Trading Busters", "Cómo trata los datos la app de Trading Busters.", """
<h1>Política de privacidad</h1><p class="lead">Fecha de entrada en vigor: {UPDATED}</p>
<p>Esta política explica cómo trata la información Trading Busters ("nosotros") cuando la app Trading Busters Publisher
accede a YouTube, TikTok, Instagram y Facebook en nuestro nombre. Trading Busters se gestiona desde España.
Contacto: {MAIL}.</p>
<h2>Quién usa la app</h2><p>La app es una herramienta interna. Solo la usa el equipo de Trading Busters para publicar
nuestros propios vídeos en nuestras propias cuentas. No se ofrece al público y no tiene usuarios externos.</p>
<h2>Datos a los que accedemos</h2><p>Cuando un miembro del equipo inicia sesión y da permiso, la app puede acceder, solo
en nuestras propias cuentas, a:</p>
<ul><li><strong>YouTube</strong> (permisos <code>youtube.upload</code> y <code>youtube</code>): subir vídeos a nuestro propio
canal y leer la información y las estadísticas de los vídeos de nuestro propio canal.</li>
<li><strong>TikTok</strong> (permisos <code>user.info.basic</code>, <code>user.info.stats</code> y <code>video.upload</code>):
leer el perfil básico y el número de seguidores de nuestra propia cuenta, y enviar vídeos que hemos hecho a nuestra
propia bandeja de TikTok como borradores. Cada borrador lo revisamos y lo publicamos nosotros en la app de TikTok.</li>
<li><strong>Instagram y Facebook</strong> (permisos <code>instagram_basic</code>, <code>instagram_content_publish</code>,
<code>pages_show_list</code>, <code>pages_read_engagement</code>, <code>pages_manage_posts</code> y, si se conceden,
<code>instagram_manage_insights</code> y <code>read_insights</code>): publicar nuestros propios vídeos en nuestra propia
cuenta de Instagram y página de Facebook, y leer su información básica, interacciones y visualizaciones.</li></ul>
<h2>Para qué lo usamos</h2><p>Usamos este acceso solo para publicar los vídeos de Trading Busters en nuestras propias
cuentas y para medir cómo funcionan nuestros propios vídeos. No lo usamos para publicidad, no lo vendemos y no lo
compartimos con terceros, salvo lo necesario para entregarlo a las propias plataformas.</p>
<h2>Política de datos de usuario de los servicios de API de Google</h2><p>El uso y la transferencia por parte de Trading
Busters de la información recibida de las API de Google cumplen la
<a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services User Data Policy</a>,
incluidos los requisitos de uso limitado (Limited Use). La app usa los
<a href="https://developers.google.com/youtube/terms/api-services-terms-of-service">servicios de la API de YouTube</a>; al
usar la app también aceptas las <a href="https://www.youtube.com/t/terms">condiciones de servicio de YouTube</a> y la
<a href="https://policies.google.com/privacy">política de privacidad de Google</a>.</p>
<h2 id="youtube">Servicios de la API de YouTube</h2>
<p>Trading Busters Publisher usa los <a href="https://developers.google.com/youtube/terms/api-services-terms-of-service">servicios
de la API de YouTube</a>. Al usar la app aceptas quedar vinculado por las
<a href="https://www.youtube.com/t/terms">condiciones de servicio de YouTube</a>; lee también la
<a href="https://policies.google.com/privacy">política de privacidad de Google</a>.</p>
<ul><li><strong>A qué accede:</strong> solo a nuestro propio canal de YouTube: su nombre e identificador, los vídeos que
subimos y sus estadísticas públicas (visualizaciones, me gusta, comentarios).</li>
<li><strong>Qué guarda:</strong> el token OAuth de nuestro canal, los identificadores de los vídeos que subimos e
instantáneas de sus estadísticas, para saber cuándo llegan mejor a la gente.</li>
<li><strong>Cómo se usa y se comparte:</strong> solo para publicar nuestros vídeos y medirlos. No se comparte con nadie,
interno ni externo, y no se usa para publicidad.</li>
<li><strong>Cookies y almacenamiento en el dispositivo:</strong> la app funciona en nuestro propio servidor y no guarda
nada en los dispositivos de los visitantes; esta web no usa cookies.</li>
<li><strong>Revocar el acceso:</strong> se puede revocar en cualquier momento en la
<a href="https://security.google.com/settings/security/permissions">página de seguridad de Google</a>
(<a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a>).</li>
<li><strong>Eliminación:</strong> si se revoca el acceso, borramos el token guardado y los datos de YouTube anteriores en
un plazo de 7 días. Guardamos las estadísticas de nuestros propios vídeos solo mientras la app siga autorizada. Para
pedir la eliminación en cualquier momento, escribe a {MAIL}.</li></ul>
<h2>TikTok</h2><p>Nuestro uso de TikTok cumple las
<a href="https://www.tiktok.com/legal/page/global/tik-tok-developer-terms-of-service/en">condiciones de servicio para
desarrolladores de TikTok</a>. No recogemos datos de otros usuarios de TikTok. El acceso se puede revocar en la app de
TikTok, en Ajustes y privacidad &rarr; Seguridad &rarr; Apps y servicios.</p>
<h2>Meta (Instagram y Facebook)</h2><p>Nuestro uso de Instagram y Facebook cumple las
<a href="https://developers.facebook.com/terms/">condiciones de la plataforma de Meta</a>. El acceso se puede retirar en
Facebook, en Configuración &rarr; Integraciones comerciales.</p>
<h2>Almacenamiento y seguridad</h2><p>Los tokens de acceso se guardan de forma privada en infraestructura que controla
Trading Busters, nunca se comparten ni se venden y solo se usan para lo descrito arriba. La app no recoge datos
personales de espectadores ni de otros usuarios. Esta web no usa cookies, analítica ni rastreadores.</p>
<h2>Conservación y eliminación</h2><p>Guardamos los tokens solo mientras la app está en uso. El acceso de Google se puede
revocar en cualquier momento en <a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a>.
Para pedirnos que borremos cualquier dato guardado, escribe a {MAIL}; lo haremos en un plazo de 30 días.</p>
<h2>Tus derechos</h2><p>Según el RGPD puedes pedir el acceso, la rectificación o la supresión de tus datos personales, y
puedes reclamar ante la Agencia Española de Protección de Datos (AEPD).</p>
<h2>Cambios</h2><p>Si esta política cambia, actualizaremos esta página y la fecha de arriba.</p>
""")

page("terms", "Condiciones de uso - Trading Busters", "Condiciones de la web y de la app de Trading Busters.", """
<h1>Condiciones de uso</h1><p class="lead">Fecha de entrada en vigor: {UPDATED}</p>
<p>Estas condiciones se aplican a la web de Trading Busters y a la app Trading Busters Publisher. Al usarlas aceptas
estas condiciones.</p>
<h2>El servicio</h2><p>Trading Busters Publisher es una herramienta interna que usa el equipo de Trading Busters para
publicar nuestros propios vídeos en nuestro propio canal de YouTube y en nuestras cuentas de TikTok, Instagram y
Facebook. No tiene usuarios externos; el acceso está limitado a miembros autorizados del equipo.</p>
<h2>Servicios de terceros</h2><p>La app usa los servicios de la API de YouTube, la Content Posting API de TikTok y la
Graph API de Meta. Su uso también está sujeto a las <a href="https://www.youtube.com/t/terms">condiciones de servicio de
YouTube</a>, la <a href="https://policies.google.com/privacy">política de privacidad de Google</a>, las
<a href="https://www.tiktok.com/legal/page/global/terms-of-service/en">condiciones de servicio de TikTok</a> y las
<a href="https://developers.facebook.com/terms/">condiciones de la plataforma de Meta</a>.</p>
<h2>Uso aceptable</h2><p>No puedes usar la app para subir contenido sobre el que no tengas derechos, para incumplir las
políticas de una plataforma ni para acceder a cuentas o datos que no sean tuyos.</p>
<h2>Contenido</h2><p>Los vídeos, textos e imágenes de Trading Busters son nuestros salvo que se indique lo contrario.
Nuestros vídeos son informativos: no son consejo financiero, legal ni de inversión, y no vendemos productos financieros,
cursos ni señales.</p>
<h2>Sin garantía</h2><p>La web y la app se ofrecen "tal cual", sin garantías de ningún tipo. En la medida en que lo
permita la ley, Trading Busters no responde de daños indirectos o consecuentes derivados de su uso.</p>
<h2>Cambios y terminación</h2><p>Podemos cambiar estas condiciones o dejar de ofrecer la app en cualquier momento. Los
cambios se publicarán en esta página.</p>
<h2>Ley aplicable</h2><p>Estas condiciones se rigen por la legislación española.</p>
<h2>Contacto</h2><p>{MAIL}</p>
""")

page("tiktok-callback", "Autorización - Trading Busters", "Página de retorno de la autorización de la app de Trading Busters.", """
<h1>Autorización</h1>
<p id="msg" class="lead">Leyendo la respuesta de la autorización&hellip;</p>
<p><textarea id="code" readonly rows="3" hidden></textarea></p>
<p><button id="copy" hidden>Copiar código</button></p>
<p>Esta página solo muestra el código de un solo uso que TikTok devuelve después de autorizar la app de Trading Busters.
No envía nada a ningún sitio. Copia el código en el paso de configuración en pocos minutos: caduca y solo sirve una vez.</p>
<script>
const q = new URLSearchParams(location.search), msg = document.getElementById('msg'), box = document.getElementById('code'), btn = document.getElementById('copy');
if (q.get('error')) { msg.textContent = 'TikTok devolvió un error: ' + q.get('error') + ' ' + (q.get('error_description') || ''); }
else if (q.get('code')) { msg.textContent = 'Autorizado. State: ' + (q.get('state') || '(ninguno)') + '. Código:'; box.value = q.get('code'); box.hidden = btn.hidden = false;
  btn.onclick = () => { box.select(); navigator.clipboard ? navigator.clipboard.writeText(box.value) : document.execCommand('copy'); btn.textContent = 'Copiado'; }; }
else { msg.textContent = 'No hay código de autorización en esta dirección.'; }
</script>
""", robots='<meta name="robots" content="noindex">')
print("generado: index.html, privacy/, terms/, tiktok-callback/")
