for name,(h,body) in pages.items():
    main=name=='index.html'
    html=(h+NAV+'<main id="top">'+body+'</main>'+FOOT+('' if main else '</body></html>')).replace('href="#kontakt"','href="konsultacja.html"').replace('href="kontakt.html">Bezpłatna','href="konsultacja.html">Bezpłatna')
    open(OUT+'/'+name,'w').write(html)
print('ok',len(pages))
