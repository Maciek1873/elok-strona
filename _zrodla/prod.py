# Buduje gotową paczkę na serwer: out/ -> dist/
import os, re, shutil, json, html as H
from PIL import Image
import time
VER=time.strftime('%y%m%d%H%M')
SRC='out'; D='dist'; SITE='https://elok-agency.pl'
shutil.rmtree(D, ignore_errors=True); os.makedirs(D)
for d in ('img','vid'): shutil.copytree(SRC+'/'+d, D+'/'+d)
for f in ('site.css','site.js'): shutil.copy(SRC+'/'+f, D+'/'+f)
# ikony
lg=Image.open('/home/claude/elok-panel/logo_512.png').convert('RGB')
lg.resize((180,180),Image.LANCZOS).save(D+'/apple-touch-icon.png')
lg.resize((32,32),Image.LANCZOS).save(D+'/favicon-32.png')
lg.resize((512,512),Image.LANCZOS).save(D+'/icon-512.png')
lg.resize((48,48),Image.LANCZOS).save(D+'/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
shutil.copy('/tmp/claude-0/og.jpg', D+'/img/og.jpg')
TITLES={'index.html':'ELOK · Automatyzacje, strony i marketing dla firm',
 'automatyzacje.html':'Automatyzacje dla firm: panele, CRM, faktury · ELOK',
 'strony.html':'Strony internetowe i sklepy dla firm · ELOK',
 'marketing.html':'Reklamy Google, Facebook i TikTok dla firm · ELOK',
 'cennik.html':'Cennik: automatyzacje, strony i reklamy · ELOK',
 'realizacje.html':'Case studies: wdrożenia dla firm · ELOK',
 'konsultacja.html':'Bezpłatna konsultacja online (30 min) · ELOK',
 'kontakt.html':'Kontakt: telefon, e-mail, konsultacja · ELOK',
 'o-nas.html':'O nas: kim jesteśmy i jak pracujemy · ELOK'}
pages=[f for f in sorted(os.listdir(SRC)) if f.endswith('.html')]
def meta(f, h):
    t=re.search(r'<title>(.*?)</title>',h).group(1)
    if f in TITLES: h=h.replace('<title>%s</title>'%t,'<title>%s</title>'%TITLES[f],1); t=TITLES[f]
    m=re.search(r'<meta name="description" content="(.*?)">',h); desc=m.group(1) if m else ''
    url=SITE+'/' if f=='index.html' else SITE+'/'+f
    add=('<meta name="theme-color" content="#08080A"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">'
         '<link rel="canonical" href="%s"><meta property="og:type" content="website"><meta property="og:locale" content="pl_PL"><meta property="og:site_name" content="ELOK">'
         '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s"><meta property="og:image" content="%s/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">')%(url,t,desc,url,SITE)
    if f=='demo.html': add+='<meta name="robots" content="noindex">'
    return h.replace('</title>','</title>'+add,1)
for f in pages:
    h=open(SRC+'/'+f).read()
    h=h.replace('<meta name="claude:viewport-fit-sides" content="cover">','')
    if not h.lstrip().lower().startswith('<!doctype'):
        i=h.index('<header class="nav"')
        h='<!doctype html><html lang="pl"><head><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'+h[:i]+'</head><body>'+h[i:]+'</body></html>'
    h=meta(f,h)
    h=h.replace('<script src="site.js"></script>','<script src="ustawienia.js?v=%s"></script><script src="site.js?v=%s"></script>'%(VER,VER))
    h=h.replace('<link rel="stylesheet" href="site.css">','<link rel="stylesheet" href="site.css?v=%s">'%VER)
    h=h.replace('Zadzwoń: <b style="user-select:all;white-space:nowrap">455 505 820</b>','Zadzwoń: <a href="tel:+48455505820" style="color:inherit"><b style="white-space:nowrap">455 505 820</b></a>')
    h=h.replace('pod adresem: kontakt@elok-agency.pl','pod adresem: <a href="mailto:kontakt@elok-agency.pl">kontakt@elok-agency.pl</a>')
    assert '<meta name="viewport"' in h and h.count('<body')==1, f
    open(D+'/'+f,'w').write(h)
# 404
k=open(D+'/kontakt.html').read()
a=k.index('<main id="top">')+len('<main id="top">'); b=k.index('</main>')
NF=('<section class="phero"><div class="wrap"><div class="eyebrow">Błąd 404</div><h1>Tej strony <span class="g">tu nie ma.</span></h1>'
    '<p class="lead">Możliwe, że adres się zmienił po przebudowie strony. Wróć na stronę główną albo umów bezpłatną konsultację.</p>'
    '<div class="btns" style="margin-top:34px"><a class="btn pri mag" href="index.html">Strona główna <span class="ar">→</span></a><a class="btn sec" href="konsultacja.html">Bezpłatna konsultacja</a></div></div></section>')
nf=k[:a]+NF+k[b:]
nf=re.sub(r'<title>.*?</title>','<title>Nie znaleziono strony · ELOK</title>',nf,1).replace('<head>','<head><base href="/"><meta name="robots" content="noindex">',1)
nf=re.sub(r'<link rel="canonical"[^>]*>','',nf)
open(D+'/404.html','w').write(nf)
# sitemap + robots
sm=[p for p in pages if p not in ('demo.html',)]
open(D+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>%s</loc></url>\n'%(SITE+'/' if p=='index.html' else SITE+'/'+p) for p in sm)+'</urlset>\n')
open(D+'/robots.txt','w').write('User-agent: *\nAllow: /\nDisallow: /demo.html\n\nSitemap: %s/sitemap.xml\n'%SITE)
# .htaccess
OLD=[('polityka-prywatnosci','polityka-prywatnosci.html'),('regulamin','regulamin.html'),('cookies','cookies.html'),('rezerwacje','konsultacja.html'),
 ('referencje','realizacje.html'),('blog','blog.html'),('o-nas','o-nas.html'),('kontakt','kontakt.html'),('cennik','cennik.html'),('uslugi','automatyzacje.html'),
 ('marketing','marketing.html'),('development','strony.html'),('automatyzacje','automatyzacje.html'),('vip-business-launch',''),('bio',''),('404-fail',''),
 ('brief','konsultacja.html'),('brief-vip','konsultacja.html'),('marketing-brief','konsultacja.html'),('development-brief','konsultacja.html'),('automatyzacje-brief','konsultacja.html'),
 ('case-studies/serwis-samochodowy-premium','realizacja-serwis.html'),('case-studies/indywidualny-panel-firmowy','realizacja-panel.html'),('case-studies','realizacje.html'),
 ('sitemap_index\\.xml','sitemap.xml'),('wp-sitemap\\.xml','sitemap.xml'),('feed','blog.html')]
for o,n in json.load(open('blogmap.json')).items(): OLD.append((o,n+'.html'))
rules=''.join('RewriteRule ^%s/?$ https://%%{HTTP_HOST}/%s [R=301,L]\n'%(o,n) for o,n in OLD)
HT='''# ELOK – elok-agency.pl (strona bez WordPressa)
DirectoryIndex index.html index.php
ErrorDocument 404 /404.html
Options -Indexes
AddDefaultCharset UTF-8

<IfModule mod_rewrite.c>
RewriteEngine On
# bez www
RewriteCond %{HTTP_HOST} ^www\\.(.+)$ [NC]
RewriteRule ^ https://elok-agency.pl%{REQUEST_URI} [R=301,L]
# zawsze https
RewriteCond %{HTTPS} off
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]

# stare adresy z WordPressa -> nowe strony
'''+rules+'''
# adres bez .html (np. /cennik) -> /cennik.html
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{DOCUMENT_ROOT}/$1.html -f
RewriteRule ^([a-z0-9-]+)/?$ https://%{HTTP_HOST}/$1.html [R=301,L]
</IfModule>

<IfModule mod_headers.c>
# wersja testowa (test.elok-agency.pl) – niewidoczna dla Google
SetEnvIfNoCase Host "^test\\." ELOK_TEST
Header always set X-Robots-Tag "noindex, nofollow" env=ELOK_TEST
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set X-Frame-Options "SAMEORIGIN"
<FilesMatch "\\.(html)$">
Header set Cache-Control "no-cache"
</FilesMatch>
<FilesMatch "\\.(css|js)$">
Header set Cache-Control "public, max-age=86400"
</FilesMatch>
<FilesMatch "\\.(jpg|jpeg|png|webp|svg|ico|mp4)$">
Header set Cache-Control "public, max-age=2592000"
</FilesMatch>
<Files "ustawienia.js">
Header set Cache-Control "no-cache"
</Files>
</IfModule>

<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript text/javascript image/svg+xml application/xml text/plain
</IfModule>
'''
open(D+'/.htaccess','w').write(HT)
print('dist ok', len(os.listdir(D)))
