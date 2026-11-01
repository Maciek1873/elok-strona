import json, re, html as H
src = open('gen7.py').read().replace("exec(open('gen_loop.py').read())", "")
exec(src)
WP = '/tmp/claude-0/wp/'
KEEP = {'RODO','GDPR','SSL','UE','IP','HTTP','HTTPS','B2B','UX','UI','UX/UI','AI','CRM','SEO','PPC','ROAS','CPC','CTR','CPA','KPI','ELOK','NIP','EOG','USA','SMS','WWW','API','ART.','UST.','LIT.'}
def sent(t):
    if t.upper()!=t or not re.search('[A-ZĄĆĘŁŃÓŚŹŻ]{3}',t): return t
    out=[];first=True
    for w in t.split(' '):
        core=re.sub(r'[^\wĄĆĘŁŃÓŚŹŻąćęłńóśźż/.]','',w)
        if core.upper() in KEEP or re.match(r'^[A-Z]\.$|^§$|^\d',w): out.append(w)
        else:
            lw=w.lower()
            if first: lw=re.sub(r'^(\W*)(\w)',lambda m:m.group(1)+m.group(2).upper(),lw)
            out.append(lw)
        if re.search(r'\w',w) and not re.match(r'^(§|\d+\.?|[A-Z]\.)$',w): first=False
    return ' '.join(out)
def clean(c):
    c=re.sub(r'<style.*?</style>|<script.*?</script>|<!--.*?-->','',c,flags=re.S)
    c=re.sub(r'<img[^>]*>','',c)
    c=re.sub(r'</?(div|span|section|article|header|footer|i|svg|path|button|em)[^>]*>','\n',c)
    c=re.sub(r'<(h[1-4]|p|ul|ol|li|strong|b|blockquote)\b[^>]*>',r'<\1>',c)
    c=re.sub(r'<a [^>]*href="([^"]*)"[^>]*>',r'<a href="\1">',c)
    return [l.strip() for l in c.split('\n') if l.strip()]
def body_of(lines, blog):
    raw=' '.join(lines); raw=re.sub(r'\s+',' ',raw)
    i=raw.find('<h1>'); cat=re.sub('<[^>]+>','',raw[:i]).strip() if i>0 else ''
    mm=re.search(r'Obowiązuje od: [0-9.]+',raw); meta=mm.group(0) if mm else ''
    txt='\n'.join(m.group(0) for m in re.finditer(r'<(h[1-4]|p|ul|ol|blockquote)>.*?</\1>',raw))
    txt=re.sub(r'<h1>.*?</h1>','',txt,count=1,flags=re.S)
    m=re.match(r'\s*<p>(.*?)</p>',txt,re.S); lead=m.group(1).strip() if m else ''
    if m: txt=txt[m.end():]
    if blog:  # stare CTA na końcu
        i=txt.rfind('<h3>'); 
        if i>0 and '<a href' in txt[i:]: txt=txt[:i]
    txt=re.sub(r'<(h[23])>(.*?)</\1>',lambda m:'<%s>%s</%s>'%(m.group(1),sent(m.group(2).strip()),m.group(1)),txt,flags=re.S)
    txt=txt.replace('Unless stated otherwise (chyba że umowa mówi inaczej), koszty','Jeśli umowa nie mówi inaczej, koszty')
    txt=txt.replace('href="/kontakt/"','href="konsultacja.html"')
    txt=re.sub(r'<p>\s*','<p>',txt); txt=re.sub(r'\s*</p>','</p>',txt)
    return cat, meta, lead, txt
def art_page(crumb, eyebrow, h1, lead, inner, extra=''):
    return ('<section class="phero"><div class="wrap"><div class="crumbs"><a href="index.html">ELOK</a> / %s</div><div class="eyebrow">%s</div><h1 class="ah1">%s</h1>%s</div></section>'
            '<section style="padding-top:0"><div class="wrap"><article class="art">%s</article>%s</div></section>')%(crumb,eyebrow,h1,('<p class="lead">%s</p>'%lead) if lead else '',inner,extra)
# ---------- strony prawne ----------
LEG={'polityka-prywatnosci':('Polityka prywatności','Zasady przetwarzania danych osobowych w serwisie elok-agency.pl.'),
     'regulamin':('Regulamin współpracy','Zasady współpracy z ELOK.'),
     'cookies':('Polityka cookies','Jak serwis elok-agency.pl korzysta z plików cookies.')}
for slug,(t,desc) in LEG.items():
    d=json.load(open(WP+slug+'.json')); cat,meta,lead,txt=body_of(clean(d['content']),False)
    pages[slug+'.html']=(head(t+' · ELOK',desc), art_page(t,'Dokumenty',t,(meta+'.') if meta else '', '<div class="legaltxt">'+txt+'</div>'))
# ---------- blog ----------
BLOG=[('sprzedaz-na-sterydach','blog-sprzedaz-na-sterydach'),('automatyzacja-to-nie-tylko-oszczednosc-czasu-to-jedyny-sposob-na-skalowanie-bez-chaosu','blog-automatyzacja-skalowanie'),
 ('tani-wordpress-to-najdrozsza-inwestycja-dlaczego-jakosc-kodu-wplywa-na-twoje-przychody','blog-tani-wordpress'),('reklama-to-nie-hazard-dlaczego-twoje-kampanie-na-facebooku-i-google-nie-dowoza-wynikow','blog-reklama-to-nie-hazard'),
 ('marketingiem-nie-naprawisz-slabego-produktu-ale-bez-niego-nikt-nie-pozna-tego-dobrego','blog-marketing-i-produkt'),('facebook-ads-w-2025-dlaczego-twoje-stare-strategie-przestaly-dzialac-i-jak-to-naprawic','blog-facebook-ads'),
 ('google-ads-to-matematyka-nie-magia-jak-przestac-placic-podatek-od-niewiedzy','blog-google-ads')]
MC=['stycznia','lutego','marca','kwietnia','maja','czerwca','lipca','sierpnia','września','października','listopada','grudnia']
CATN={'AI & TECH':'Automatyzacje','DEVELOPMENT':'Strony','MARKETING':'Marketing','GOOGLE ADS':'Google Ads','FACEBOOK ADS':'Facebook Ads','MARKETING & ADS':'Marketing'}
cards=[]; OLD2NEW={}
for old,new in BLOG:
    d=json.load(open(WP+old+'.json')); cat,meta,lead,txt=body_of(clean(d['content']),True)
    y,mo,da=d['date'][:10].split('-'); dt='%d %s %s'%(int(da),MC[int(mo)-1],y)
    c=CATN.get(cat.strip().upper(), sent(cat.strip()) or 'Blog')
    title=H.unescape(d['title']).rstrip('.')
    cta=('<div class="artcta rv"><div><b>Chcesz to wdrożyć u siebie?</b><span>30 minut online, bez zobowiązań. Pokażemy, co da się usprawnić w Twojej firmie.</span></div>'
         '<a class="btn pri mag" href="konsultacja.html">Umów bezpłatną konsultację <span class="ar">→</span></a></div>')
    inner='<div class="artmeta">%s · %s</div>%s'%(c,dt,txt)
    pages[new+'.html']=(head(title+' · Blog ELOK', H.escape(re.sub('<[^>]+>','',lead))[:155]), art_page('<a href="blog.html">Blog</a>', c, title, lead, inner, cta))
    cards.append('<a class="bcard rv" href="%s.html"><span class="tg">%s · %s</span><h3>%s</h3><p>%s</p><span class="more">Czytaj <span class="ar">→</span></span></a>'%(new,c,dt,title,re.sub('<[^>]+>','',lead)))
    OLD2NEW[old]=new
pages['blog.html']=(head('Blog · ELOK','Artykuły o automatyzacjach, stronach i marketingu dla firm.'),
    '<section class="phero"><div class="wrap"><div class="crumbs"><a href="index.html">ELOK</a> / Blog</div><div class="eyebrow">Blog</div><h1>Krótko o tym, <span class="g">co działa.</span></h1><p class="lead">Automatyzacje, strony i reklamy bez lania wody.</p></div></section>'
    '<section style="padding-top:0"><div class="wrap"><div class="bgrid">'+''.join(cards)+'</div></div></section>')
json.dump(OLD2NEW,open('blogmap.json','w'))
# ---------- stopka: linki, telefon i mail klikalne ----------
FOOT=FOOT.replace('<a href="#">Polityka prywatności</a> · <a href="#">Regulamin</a> · <a href="#">Cookies</a>','<a href="polityka-prywatnosci.html">Polityka prywatności</a> · <a href="regulamin.html">Regulamin</a> · <a href="cookies.html">Cookies</a>')
FOOT=FOOT.replace('<span style="user-select:all">455 505 820</span>','<a href="tel:+48455505820">455 505 820</a>').replace('<span style="user-select:all">kontakt@elok-agency.pl</span>','<a href="mailto:kontakt@elok-agency.pl">kontakt@elok-agency.pl</a>')
FOOT=FOOT.replace('<a href="konsultacja.html">Konsultacja</a></div>','<a href="konsultacja.html">Konsultacja</a><a href="blog.html">Blog</a></div>',1)
assert 'polityka-prywatnosci.html' in FOOT and 'tel:+48' in FOOT and 'blog.html' in FOOT
# ---------- kontakt: zadzwoń / napisz ----------
h,b=pages['kontakt.html']
b=b.replace('<div class="big">455 505 820</div>','<a class="big" href="tel:+48455505820">455 505 820</a>').replace('<div class="big">kontakt@elok-agency.pl</div>','<a class="big" href="mailto:kontakt@elok-agency.pl">kontakt@elok-agency.pl</a>')
b=b.replace('<button class="btn sec" type="button" data-copy="455505820">Kopiuj numer</button>','<div class="cbt"><a class="btn pri" href="tel:+48455505820">Zadzwoń</a><button class="btn sec" type="button" data-copy="455505820">Kopiuj numer</button></div>')
b=b.replace('<button class="btn sec" type="button" data-copy="kontakt@elok-agency.pl">Kopiuj adres</button>','<div class="cbt"><a class="btn pri" href="mailto:kontakt@elok-agency.pl">Napisz maila</a><button class="btn sec" type="button" data-copy="kontakt@elok-agency.pl">Kopiuj adres</button></div>')
assert b.count('class="cbt"')==2
pages['kontakt.html']=(h,b)
# ---------- konsultacja: prawdziwa wysyłka ----------
h,b=pages['konsultacja.html']
o1='<p class="note" style="font-size:14px">Potwierdzenie z linkiem do rozmowy wyślemy na Twój e-mail. Wysyłając, zgadzasz się na kontakt w sprawie konsultacji.</p></form>'
assert o1 in b
b=b.replace(o1,'<input type="text" name="www2" id="b-www2" class="hpf" tabindex="-1" autocomplete="off" aria-hidden="true"><div class="berr" id="berr" role="alert" hidden></div>'
  '<p class="note" style="font-size:14px">Potwierdzenie przyjdzie od razu na Twój e-mail. Wysyłając, zgadzasz się na kontakt w sprawie konsultacji. Szczegóły: <a href="polityka-prywatnosci.html">polityka prywatności</a>.</p></form>')
o2='Potwierdzenie z linkiem do rozmowy wyślemy na Twój e-mail.</p></div>'
assert o2 in b
b=b.replace(o2,'Potwierdzenie wysłaliśmy na Twój e-mail. Jeśli go nie widzisz, zajrzyj do folderu Spam albo zadzwoń: <a href="tel:+48455505820">455 505 820</a>.</p></div>')
pages['konsultacja.html']=(h,b)
# reszta stron: „link do rozmowy” w tekstach
for k,(h,b) in list(pages.items()):
    pages[k]=(h,b.replace('Potwierdzenie z linkiem do rozmowy','Potwierdzenie'))
exec(open('gen_loop.py').read())
