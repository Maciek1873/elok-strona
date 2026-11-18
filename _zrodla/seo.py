# SEO: dane strukturalne (JSON-LD), tytuły, opisy. Uruchamiać z katalogu głównego strony:
#   python3 _zrodla/seo.py
# Bezpieczne do ponownego uruchomienia (blok JSON-LD jest podmieniany między znacznikami).
import re, json, html, glob, os
B = 'https://elok-agency.pl'
ORG_ID = B + '/#firma'
ORG = {
  "@type": "ProfessionalService", "@id": ORG_ID, "name": "ELOK", "alternateName": "ELOK Agency",
  "legalName": "Carbonmiledesign Sp. z o.o.", "url": B + "/", "logo": B + "/icon-512.png",
  "image": B + "/img/og.jpg", "telephone": "+48455505820", "email": "kontakt@elok-agency.pl",
  "taxID": "1231588867",
  "address": {"@type": "PostalAddress", "streetAddress": "ul. Borowa 44", "postalCode": "05-520",
              "addressLocality": "Konstancin-Jeziorna", "addressRegion": "mazowieckie", "addressCountry": "PL"},
  "areaServed": {"@type": "Country", "name": "Polska"},
  "knowsAbout": ["automatyzacja procesów", "strony internetowe", "sklepy internetowe", "integracje API",
                 "systemy dla serwisów samochodowych", "integracja z Allegro", "Google Ads", "Facebook Ads"],
  "sameAs": ["https://www.instagram.com/elok.agency", "https://www.tiktok.com/@elok.agency"],
}
WEBSITE = {"@type": "WebSite", "@id": B + "/#strona", "url": B + "/", "name": "ELOK", "inLanguage": "pl-PL",
           "publisher": {"@id": ORG_ID}}

# Tytuły i opisy do poprawy (plik: (title, description)); None = bez zmian
META = {
 'blog.html': ('Blog ELOK: automatyzacje, strony i reklamy w praktyce',
   'Praktyczne artykuły o automatyzacji pracy w firmie, stronach, które sprzedają, oraz reklamach Google i Facebook. Bez teorii, z przykładami z wdrożeń.'),
 'blog-automatyzacja-skalowanie.html': ('Automatyzacja w firmie: jak rosnąć bez chaosu · ELOK', None),
 'blog-facebook-ads.html': ('Facebook Ads: dlaczego stare strategie nie działają · ELOK', None),
 'blog-google-ads.html': ('Google Ads bez przepalania budżetu · ELOK', None),
 'blog-marketing-i-produkt.html': ('Marketing czy produkt: co naprawić najpierw · ELOK', None),
 'blog-reklama-to-nie-hazard.html': ('Dlaczego reklamy w Google i na Facebooku nie działają · ELOK', None),
 'blog-tani-wordpress.html': ('Tani WordPress: dlaczego wychodzi najdrożej · ELOK', None),
 'konsultacja.html': (None, 'Bezpłatna, niezobowiązująca rozmowa online (30 minut) o automatyzacji, stronie albo reklamach. Wybierz termin w kalendarzu, link do spotkania dostaniesz mailem.'),
 'marketing.html': (None, 'Kampanie Google Ads, Facebook i TikTok dla firm, prowadzone na podstawie danych. Mierzymy telefony i zapytania, a nie tylko kliknięcia. Bezpłatna konsultacja.'),
 'realizacja-panel.html': (None, 'Panel finansowy dla dwóch sklepów w jednej spółce: raport kasowy, oferty i podatki liczone osobno dla każdej marki. Zobacz, jak działa.'),
 'realizacja-serwis.html': ('Case study: system wycen dla serwisu samochodowego · ELOK', 'System dla serwisu samochodowego: od katalogu części przez wycenę i ofertę PDF wysłaną mailem do faktury, bez przepisywania. Czas wyceny krótszy o 87%.'),
 'realizacje.html': (None, 'Case studies ELOK: aplikacja do Allegro, system wycen dla serwisu, zautomatyzowany sklep z częściami i panel finansowy. Zobacz, jak działają nasze wdrożenia.'),
 'kontakt.html': (None, 'Kontakt z ELOK: telefon +48 455 505 820, kontakt@elok-agency.pl, Konstancin-Jeziorna. Pracujemy z firmami z całej Polski, zdalnie. Umów bezpłatną konsultację.'),
 'o-nas.html': (None, 'ELOK to zespół, który buduje automatyzacje, systemy, strony i kampanie reklamowe dla firm. Zobacz, jak pracujemy i co już zrobiliśmy dla klientów.'),
 'cennik.html': (None, 'Cennik ELOK: automatyzacje od 600 zł, strony od 1 500 zł, sklepy od 2 500 zł, reklamy od 700 zł miesięcznie. Ceny netto, stała cena ustalona przed startem.'),
 'automatyzacja-ai/index.html': (None, 'Wdrażamy automatyzacje i AI w firmach: faktury, maile, oferty, zamówienia i raporty, które robią się same. Automatyzacje od 600 zł netto. Bezpłatna konsultacja.'),
}
SERVICES = {
 'strony.html': ('Strony internetowe i sklepy dla firm', 'Strona internetowa'),
 'automatyzacje.html': ('Automatyzacja procesów i dedykowane systemy', 'Automatyzacja procesów biznesowych'),
 'marketing.html': ('Reklamy Google, Facebook i TikTok', 'Marketing internetowy'),
 'strona-dla-firmy/index.html': ('Strona internetowa dla firmy', 'Strona internetowa'),
 'automatyzacja-ai/index.html': ('Automatyzacja i AI w firmie', 'Automatyzacja procesów biznesowych'),
 'sklep-internetowy/index.html': ('Sklep internetowy', 'Sklep internetowy'),
}
CRUMB = {'strony.html':'Strony i sklepy','automatyzacje.html':'Automatyzacje','marketing.html':'Marketing','cennik.html':'Cennik',
 'o-nas.html':'O nas','kontakt.html':'Kontakt','konsultacja.html':'Konsultacja','blog.html':'Blog','realizacje.html':'Case studies',
 'regulamin.html':'Regulamin','cookies.html':'Cookies','polityka-prywatnosci.html':'Polityka prywatności',
 'strona-dla-firmy/index.html':'Strona dla firmy','automatyzacja-ai/index.html':'Automatyzacja i AI','sklep-internetowy/index.html':'Sklep internetowy'}

def txt(x): return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', x))).strip()
def url_of(f): return B + '/' + (f[:-len('index.html')] if f.endswith('index.html') else f)

def faq(s):
    out = []
    for q, a in re.findall(r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>', s, re.S):
        q, a = txt(q), txt(a)
        if q and a: out.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    return out

def setmeta(s, f):
    t, d = META.get(f, (None, None))
    if t:
        s = re.sub(r'<title>.*?</title>', '<title>' + html.escape(t, quote=False) + '</title>', s, count=1, flags=re.S)
        s = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + html.escape(t), s, count=1)
    if d:
        s = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + html.escape(d), s, count=1)
        s = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + html.escape(d), s, count=1)
    return s

def graph(s, f):
    title = txt(re.search(r'<title>(.*?)</title>', s, re.S).group(1))
    m = re.search(r'<meta name="description" content="([^"]*)"', s); desc = html.unescape(m.group(1)) if m else ''
    m = re.search(r'<meta property="og:image" content="([^"]*)"', s); img = m.group(1) if m else B + '/img/og.jpg'
    u = url_of(f); g = []
    if f == 'index.html':
        g += [ORG, WEBSITE]
    else:
        name = CRUMB.get(f)
        items = [{"@type": "ListItem", "position": 1, "name": "Strona główna", "item": B + "/"}]
        if f.startswith('realizacja-'):
            items.append({"@type": "ListItem", "position": 2, "name": "Case studies", "item": B + "/realizacje.html"})
            name = txt(re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1))
        if f.startswith('blog-'):
            items.append({"@type": "ListItem", "position": 2, "name": "Blog", "item": B + "/blog.html"})
            name = txt(re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1))
        items.append({"@type": "ListItem", "position": len(items) + 1, "name": name or title.split(' · ')[0], "item": u})
        g.append({"@type": "BreadcrumbList", "itemListElement": items})
    if f in SERVICES:
        n, typ = SERVICES[f]
        g.append({"@type": "Service", "name": n, "serviceType": typ, "description": desc, "url": u,
                  "provider": {"@id": ORG_ID}, "areaServed": {"@type": "Country", "name": "Polska"}})
    if f.startswith('blog-'):
        h1 = txt(re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1))
        g.append({"@type": "BlogPosting", "headline": h1[:110], "description": desc, "image": img, "url": u,
                  "mainEntityOfPage": u, "datePublished": "2025-12-18", "inLanguage": "pl-PL",
                  "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}})
    if f.startswith('realizacja-'):
        h1 = txt(re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1))
        g.append({"@type": "Article", "headline": h1[:110], "description": desc, "image": img, "url": u,
                  "mainEntityOfPage": u, "inLanguage": "pl-PL", "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}})
    q = faq(s)
    if q: g.append({"@type": "FAQPage", "mainEntity": q})
    if f != 'index.html': g.append({"@type": "ProfessionalService", "@id": ORG_ID, "name": "ELOK", "url": B + "/"})
    return {"@context": "https://schema.org", "@graph": g}

SKIP = {'404.html', 'demo.html'}
files = [f for f in glob.glob('*.html') if f not in SKIP] + [d + '/index.html' for d in ('strona-dla-firmy', 'automatyzacja-ai', 'sklep-internetowy') if os.path.exists(d + '/index.html')]
for f in sorted(files):
    s = open(f, encoding='utf-8').read()
    if 'noindex' in s: continue
    s = setmeta(s, f)
    s = re.sub(r'<!--seo-ld-->.*?<!--/seo-ld-->', '', s, flags=re.S)
    ld = '<!--seo-ld--><script type="application/ld+json">' + json.dumps(graph(s, f), ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script><!--/seo-ld-->'
    s = s.replace('</head>', ld + '</head>', 1)
    open(f, 'w', encoding='utf-8').write(s)
    print('ok', f)
