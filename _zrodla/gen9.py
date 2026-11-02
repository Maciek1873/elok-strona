src = open('gen8.py').read().replace("exec(open('gen_loop.py').read())", "")
exec(src)
# nowe dokumenty prawne (1.11.2026)
LEG2={'polityka-prywatnosci':('Polityka prywatności','Jakie dane zbiera ELOK, po co i jakie masz prawa.'),
      'regulamin':('Regulamin współpracy','Zasady współpracy z ELOK: konsultacja, wycena, realizacja, płatności i prawa autorskie.'),
      'cookies':('Polityka cookies','Jakie informacje strona zapisuje w przeglądarce i jak to zmienić.')}
for slug,(t,desc) in LEG2.items():
    inner=open('legal/%s.html'%slug).read()
    pages[slug+'.html']=(head(t+' · ELOK',desc), art_page(t,'Dokumenty',t,'Obowiązuje od 1 listopada 2026.','<div class="legaltxt">'+inner+'</div>'))
FOOT=FOOT.replace('<a href="cookies.html">Cookies</a>','<a href="cookies.html">Cookies</a> · <a href="#" data-cookies>Ustawienia cookies</a>',1)
assert 'data-cookies' in FOOT
exec(open('gen_loop.py').read())
