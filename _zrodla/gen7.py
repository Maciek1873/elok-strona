src = open('gen6.py').read().replace("exec(open('gen_loop.py').read())", "")
exec(src)
R=[('Sklep internetowy · Tanie Oryginały','Sklep internetowy · części BMW i MINI'),
 ('/ Tanie Oryginały</div>','/ Sklep z częściami</div>'),
 ('Tanie Oryginały to sklep z oryginalnymi częściami BMW i MINI.','Sklep internetowy z oryginalnymi częściami BMW i MINI.'),
 ('Podgląd sklepu Tanie Oryginały','Podgląd sklepu'),('<b>Tanie Oryginały</b>','<b>Twój sklep</b>'),
 ('sklep Tanie Oryginały','sklep z częściami BMW i MINI'),
 ('<div style="margin-top:26px"><a class="linkout" href="https://tanieoryginaly.pl" target="_blank" rel="noopener">Zobacz sklep na żywo: tanieoryginaly.pl ↗</a></div>','')]
for k,(h,b) in list(pages.items()):
    for a,c in R: h=h.replace(a,c); b=b.replace(a,c)
    pages[k]=(h,b)
exec(open('gen_loop.py').read())
