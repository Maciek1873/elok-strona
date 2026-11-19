/* Formularz szybkiej wyceny na landingach. Wysyła do panelu (Zgłoszenia + powiadomienie na telefon). Na wersji testowej tylko udaje wysyłkę. */
(function(){
 /* poprawki pod podkatalog: link w pasku cookies, pasek wersji testowej */
 [].forEach.call(document.querySelectorAll('.cookie a[href="cookies.html"]'),function(a){a.setAttribute('href','/cookies.html');});
 if(/^test\./.test(location.hostname)){var h=document.querySelector('.lh');if(h)h.style.top='32px';}
 /* klik w numer telefonu: zdarzenie w statystykach */
 document.addEventListener('click',function(e){var a=e.target.closest?e.target.closest('a[href^="tel:"]'):null;if(!a)return;try{if(window.gtag)gtag('event','klik_telefon');if(window.elokEv)elokEv('klik_telefon');}catch(x){}});
 /* wybór tematu jako przyciski */
 [].forEach.call(document.querySelectorAll('.chips'),function(g){var h=document.getElementById('lp-co');g.addEventListener('click',function(e){var b=e.target.closest('.chip');if(!b)return;
  [].forEach.call(g.querySelectorAll('.chip'),function(c){c.classList.toggle('on',c===b);c.setAttribute('aria-pressed',c===b?'true':'false');});if(h)h.value=b.textContent;});});
 var f=document.getElementById('lpform');if(!f)return;
 var API='https://panel.elok-agency.pl/strona/',LIVE=/^(www\.)?elok-agency\.pl$/.test(location.hostname);
 var err=document.getElementById('lperr'),done=document.getElementById('lpdone'),btn=f.querySelector('button[type=submit]'),t0=Math.floor(Date.now()/1000);
 var src=f.getAttribute('data-zrodlo')||'landing';
 function v(id){var e=document.getElementById(id);return e?e.value.trim():'';}
 function show(m){err.innerHTML=m;err.hidden=false;}
 function ok(){f.style.display='none';done.style.display='block';
  try{if(window.elokEv)elokEv('lead_'+src);if(window.elokKonwersja)elokKonwersja();}catch(e){}
  var y=done.getBoundingClientRect().top+(window.pageYOffset||0)-100;window.scrollTo(0,y);}
 f.addEventListener('submit',function(e){e.preventDefault();err.hidden=true;
  var req=[].filter.call(f.querySelectorAll('[required]'),function(i){return !i.value.trim();});if(req.length){req[0].focus();return;}
  var tel=v('lp-tel'),mail=v('lp-mail'),isTel=tel.replace(/\D/g,'').length>=9,isMail=/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(mail);
  if(!tel&&!mail){show('Wpisz telefon albo e-mail, wystarczy jedno.');document.getElementById('lp-tel').focus();return;}
  if(tel&&!isTel){show('Numer telefonu powinien mieć 9 cyfr.');document.getElementById('lp-tel').focus();return;}
  if(mail&&!isMail){show('Sprawdź adres e-mail.');document.getElementById('lp-mail').focus();return;}
  if(!LIVE){ok();return;}
  var opis='[Landing: '+src+'] '+(v('lp-co')?'Temat: '+v('lp-co')+'. ':'')+(isTel&&!isMail?'Woli kontakt telefoniczny.':'');
  var data={a:'kontakt',imie:v('lp-imie'),email:isMail?mail:'',telefon:isTel?tel:'',firma:v('lp-firma'),opis:opis,www2:v('lp-www2'),ts:t0};
  var body=Object.keys(data).map(function(k){return encodeURIComponent(k)+'='+encodeURIComponent(data[k]);}).join('&');
  var old=btn.innerHTML;btn.disabled=true;btn.innerHTML='Wysyłam…';
  var x=new XMLHttpRequest();x.open('POST',API);x.setRequestHeader('Content-Type','application/x-www-form-urlencoded');x.timeout=20000;
  function fail(m){btn.disabled=false;btn.innerHTML=old;show(m||'Nie udało się wysłać. Spróbuj jeszcze raz albo zadzwoń: <a href="tel:+48455505820">455 505 820</a>.');}
  x.onload=function(){var r=null;try{r=JSON.parse(x.responseText);}catch(e){}if(r&&r.ok){ok();return;}fail(r&&r.error?r.error:null);};
  x.onerror=x.ontimeout=function(){fail();};x.send(body);});
})();
/* Promocja dla pierwszych klientów: liczba miejsc i rabat ustawiane w panelu (Podłączenia), zapisywane w /ustawienia.js */
(function(){
 function run(c){
  var left=+c.promo||0,max=+c.promoMax||5,rab=+c.promoRabat||50;if(left<1||rab<1||rab>90)return;
  function fmt(n){n=Math.round(n);var s=String(n);return s.length>3?s.slice(0,-3)+' '+s.slice(-3):s;}
  function word(n){if(n===1)return 'Zostało 1 miejsce';var d=n%10,t=n%100;return (d>=2&&d<=4&&(t<12||t>14))?'Zostały '+n+' miejsca':'Zostało '+n+' miejsc';}
  var L=document.querySelectorAll('.price b,.pbox b');
  for(var i=0;i<L.length;i++){var b=L[i],m=b.textContent.match(/od\s*([\d\s ]+)\s*zł/);if(!m)continue;
   var n=parseInt(m[1].replace(/\D/g,''),10);if(!n)continue;
   b.innerHTML='<span class="lp-was"><s>'+fmt(n)+' zł</s><i>-'+rab+'%</i></span>od '+fmt(n*(100-rab)/100)+' zł';}
  var txt='<b>-'+rab+'% dla '+max+' pierwszych firm.</b> '+word(left)+'. W zamian tylko zgoda na pokazanie realizacji w naszym portfolio.';
  var P=document.querySelectorAll('.hero .price,.pbox b');
  for(var j=0;j<P.length;j++){var d=document.createElement('div');d.className='lp-promo';d.innerHTML=txt;P[j].parentNode.insertBefore(d,P[j]);}
 }
 {try{var x=new XMLHttpRequest();x.open('GET','/ustawienia.js?n='+Date.now());x.onload=function(){var m=x.responseText.match(/ELOK_CFG=(\{.*\});/);if(m){try{run(JSON.parse(m[1]));}catch(e){}}};x.send();}catch(e){}}
})();
/* Animacje: wejście sekcji przy przewijaniu, powiadomienia przy formularzu, przewijanie realizacji na telefonie */
(function(){
 var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
 document.documentElement.classList.add('lp-anim');
 /* 1. elementy wjeżdżają, gdy pojawiają się na ekranie */
 var els=document.querySelectorAll('.sh,.pc,.incl,.pbox,.case,.faq details,.endbox,.lp-rc,.ticks li');
 [].forEach.call(els,function(e,i){e.classList.add('rv');var p=e.parentNode,k=[].indexOf.call(p.children,e);e.style.transitionDelay=Math.min(k,5)*70+'ms';});
 if(RM||!('IntersectionObserver' in window)){[].forEach.call(els,function(e){e.classList.add('in');});}
 else{var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}});},{rootMargin:'0px 0px -8% 0px'});[].forEach.call(els,function(e){io.observe(e);});}
 /* 2. przykładowe powiadomienie na telefonie, które pokazuje, jak działa to, co robimy */
 var fc=document.querySelector('.fcard'),fm=document.getElementById('lpform');
 if(fc&&fm){var src=fm.getAttribute('data-zrodlo')||'strona';
  var M={strona:[['Nowe zapytanie ze strony','Anna: proszę o wycenę strony'],['Nowe zapytanie ze strony','Tomasz zostawił numer telefonu'],['Klient czeka na kontakt','zapytanie sprzed 2 minut']],
   sklep:[['Nowe zamówienie #1043','opłacone, etykieta gotowa'],['Stany zaktualizowane','ceny z hurtowni pobrane w nocy'],['Faktura wysłana','zamówienie #1042, automatycznie']],
   automatyzacja:[['Faktura wysłana automatycznie','klient dostał ją mailem'],['Oferta gotowa w 1 minutę','PDF wysłany do klienta'],['Przypomnienie wysłane','klient potwierdził wizytę']]}[src]||[];
  if(M.length){var n=document.createElement('div');n.className='lp-ntf';n.setAttribute('aria-hidden','true');
   n.innerHTML='<span class="lp-ni"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 16v-5a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 20.5a2 2 0 0 0 4 0"/></svg></span><span class="lp-nt"><b></b><small></small></span><em>teraz</em>';
   fc.style.position='relative';fc.appendChild(n);var i=0,b=n.querySelector('b'),s=n.querySelector('small');
   function show(){b.textContent=M[i][0];s.textContent=M[i][1];n.classList.remove('on');void n.offsetWidth;n.classList.add('on');i=(i+1)%M.length;}
   setTimeout(show,1200);if(!RM)setInterval(show,4200);}}
 /* 3. realizacje na telefonie przesuwają się same, dopóki ktoś ich nie dotknie */
 var rs=document.querySelector('.lp-rs');
 if(rs&&!RM){var stop=false;['touchstart','mousedown','wheel'].forEach(function(ev){rs.addEventListener(ev,function(){stop=true;},{passive:true});});
  setInterval(function(){if(stop||rs.scrollWidth<=rs.clientWidth+4)return;var c=rs.querySelector('.lp-rc');if(!c)return;var w=c.offsetWidth+12;
   rs.scrollTo({left:(rs.scrollLeft+w+4>=rs.scrollWidth-rs.clientWidth+w)?0:rs.scrollLeft+w,behavior:'smooth'});},3200);}
})();
