(function(){
var red=matchMedia('(prefers-reduced-motion: reduce)').matches;
function $(s,r){return (r||document).querySelector(s);}
function $$(s,r){return [].slice.call((r||document).querySelectorAll(s));}

/* nawigacja */
var nav=$('#nav');
function onS(){nav.classList.toggle('sc',scrollY>20);}addEventListener('scroll',onS,{passive:true});onS();
var bg=$('#burger');if(bg)bg.addEventListener('click',function(){var o=nav.classList.toggle('open');bg.setAttribute('aria-expanded',o);});
var here=(location.pathname.split('/').pop()||'index.html');
$$('.nav .menu a, .mob a').forEach(function(a){if(a.getAttribute('href')===here)a.classList.add('cur');});

/* sieć w hero */
var cv=$('#net');
if(cv){var cx=cv.getContext('2d'),W,H,DPR=Math.min(2,devicePixelRatio||1),P=[],pk=[],mx=-999,my=-999,D=150;
  var rs=function(){W=cv.clientWidth;H=cv.clientHeight;cv.width=W*DPR;cv.height=H*DPR;cx.setTransform(DPR,0,0,DPR,0,0);var n=Math.round(Math.min(90,W*H/16000));P=[];for(var i=0;i<n;i++)P.push({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.25,vy:(Math.random()-.5)*.25,r:Math.random()*1.6+.6});};
  rs();addEventListener('resize',rs);
  cv.parentNode.addEventListener('pointermove',function(e){var b=cv.getBoundingClientRect();mx=e.clientX-b.left;my=e.clientY-b.top;});
  cv.parentNode.addEventListener('pointerleave',function(){mx=my=-999;});
  var frame=function(){cx.clearRect(0,0,W,H);
    for(var i=0;i<P.length;i++){var p=P[i];if(!red){p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1;var dx=mx-p.x,dy=my-p.y,dd=Math.sqrt(dx*dx+dy*dy);if(dd<180&&dd>1){p.x+=dx/dd*.35;p.y+=dy/dd*.35;}}}
    for(var i=0;i<P.length;i++)for(var j=i+1;j<P.length;j++){var a=P[i],b=P[j],dx=a.x-b.x,dy=a.y-b.y,d=Math.sqrt(dx*dx+dy*dy);
      if(d<D){var al=1-d/D,near=Math.max(0,1-Math.hypot((a.x+b.x)/2-mx,(a.y+b.y)/2-my)/260);cx.strokeStyle='rgba(207,168,94,'+(al*.2+near*al*.5)+')';cx.lineWidth=.8;cx.beginPath();cx.moveTo(a.x,a.y);cx.lineTo(b.x,b.y);cx.stroke();if(!red&&Math.random()<.0009)pk.push({a:a,b:b,t:0});}}
    for(var i=0;i<P.length;i++){var p=P[i];cx.fillStyle='rgba(240,215,159,.75)';cx.beginPath();cx.arc(p.x,p.y,p.r,0,7);cx.fill();}
    for(var k=pk.length-1;k>=0;k--){var q=pk[k];q.t+=.018;if(q.t>=1){pk.splice(k,1);continue;}var x=q.a.x+(q.b.x-q.a.x)*q.t,y=q.a.y+(q.b.y-q.a.y)*q.t,g=cx.createRadialGradient(x,y,0,x,y,10);g.addColorStop(0,'rgba(255,230,170,.95)');g.addColorStop(1,'rgba(207,168,94,0)');cx.fillStyle=g;cx.beginPath();cx.arc(x,y,10,0,7);cx.fill();}
    if(!red)requestAnimationFrame(frame);};
  frame();}

/* rotujące słowo */
var rb=$$('#rot b'),ri=0;
if(rb.length&&!red)setInterval(function(){var o=rb[ri];o.classList.remove('on');o.classList.add('out');setTimeout(function(){o.classList.remove('out');},600);ri=(ri+1)%rb.length;rb[ri].classList.add('on');},2600);

/* taśma */
var mq=$('#mqt');if(mq)mq.innerHTML+=mq.innerHTML;

/* przykłady automatyzacji */
var IC={in:'<path d="M4 6h16v12H4z"/><path d="M4 7l8 6 8-6"/>',calc:'<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M8 15h2M12 15h2"/>',msg:'<path d="M4 5h16v11H9l-5 4z"/>',doc:'<path d="M6 3h9l4 4v14H6z"/><path d="M9 13l2 2 4-4"/>',box:'<path d="M3 7l9-4 9 4-9 4z"/><path d="M3 7v10l9 4 9-4V7"/>',cal:'<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',chart:'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',bank:'<path d="M3 10l9-6 9 6M5 10v8M10 10v8M14 10v8M19 10v8M3 20h18"/>',user:'<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>',truck:'<path d="M2 6h12v10H2zM14 10h4l3 3v3h-7"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',star:'<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>'};
window.ELOK_IC=IC;
var EX=[
 {k:'E-commerce',t:'Zamówienie obsługuje się samo',s:[['in','Zamówienie z Allegro i sklepu','wszystko w jednym miejscu','0 s'],['box','Stan magazynu','aktualizuje się wszędzie','+1 s'],['truck','Etykieta i wysyłka','klient dostaje numer paczki','+2 min'],['doc','Faktura','wystawiona i wysłana','+1 klik']],r:'Koniec ze sprzedawaniem towaru, którego nie ma.'},
 {k:'Usługi i gabinety',t:'Klient umawia się sam',s:[['cal','Rezerwacja online','klient wybiera wolny termin','0 s'],['msg','Potwierdzenie SMS','i przypomnienie dzień wcześniej','auto'],['user','Karta klienta','historia wizyt w panelu','auto'],['star','Prośba o opinię','link do Google po wizycie','+2 h']],r:'Mniej nieobecności i więcej opinii w Google.'},
 {k:'Biura rachunkowe',t:'Dokumenty bez gonienia klientów',s:[['in','Klient wrzuca dokumenty','zdjęciem lub mailem','0 s'],['user','Przypisanie do firmy','trafia do właściwego klienta','auto'],['msg','Przypomnienia o brakach','wysyłają się same','auto'],['bank','Płatności z banku','faktura sama oznaczona jako opłacona','auto']],r:'Klient widzi swoje rozliczenia w panelu, bez dzwonienia.'},
 {k:'Warsztaty i serwisy',t:'Od wyceny do faktury bez przepisywania',s:[['calc','Wycena z katalogu','części i ceny w kilka sekund','30 s'],['msg','Akceptacja SMS-em','klient klika i gotowe','+4 min'],['msg','Status naprawy','klient wie, kiedy odebrać','auto'],['doc','Faktura w KSeF','prosto z wyceny','+1 klik']],r:'Z działającego wdrożenia: czas wycen krótszy o 87%.'},
 {k:'Produkcja i budowlanka',t:'Oferta i zlecenie w jednym ciągu',s:[['in','Zapytanie ze strony','z wymiarami i zdjęciami','0 s'],['calc','Kalkulator ceny','materiał i robocizna liczą się same','+1 min'],['doc','Oferta i umowa','PDF gotowy do podpisu','+2 min'],['chart','Harmonogram','zespół widzi zadania w telefonie','auto']],r:'Ofertę wysyłasz tego samego dnia, a nie po tygodniu.'},
 {k:'Każda firma',t:'Raporty, które robią się same',s:[['chart','Dane z kilku programów','sprzedaż, koszty, reklamy','auto'],['calc','Zestawienie','liczy się co noc','03:00'],['in','Raport na maila','czeka rano w skrzynce','07:00'],['msg','Alert w telefonie','gdy coś odbiega od normy','auto']],r:'Zamiast składać Excela, czytasz wynik przy kawie.'}
];
var tabs=$('#tabs'),stage=$('#stage');
if(tabs&&stage){var cur=0,tmr=null,auto=null;
  var svg=function(k){return '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+IC[k]+'</svg>';};
  var show=function(i){cur=i;$$('button',tabs).forEach(function(b,j){b.setAttribute('aria-selected',j===i);});var e=EX[i];
    stage.innerHTML='<div class="ttl fadein"><h3>'+e.t+'</h3><span>PRZYKŁAD · '+e.k.toUpperCase()+'</span></div><div class="flowx fadein"><div class="prog"></div>'+e.s.map(function(s){return '<div class="node"><div class="ic">'+svg(s[0])+'</div><span class="t">'+s[3]+'</span><b>'+s[1]+'</b><small>'+s[2]+'</small></div>';}).join('')+'</div><div class="res fadein"><span class="pill">✓ dzieje się samo</span><p>'+e.r+'</p></div>';
    var nodes=$$('.node',stage),pg=$('.prog',stage),k=0;clearInterval(tmr);
    var step=function(){nodes.forEach(function(n,j){n.classList.toggle('on',j<=k);});pg.style.width=(k/(nodes.length-1)*88)+'%';k++;if(k>=nodes.length)clearInterval(tmr);};
    if(red){k=nodes.length-1;step();}else{step();tmr=setInterval(step,850);}};
  EX.forEach(function(e,i){var b=document.createElement('button');b.type='button';b.setAttribute('role','tab');b.textContent=e.k;b.onclick=function(){show(i);clearInterval(auto);};tabs.appendChild(b);});
  var start=+(tabs.getAttribute('data-start')||0);show(start);
  if(!red)auto=setInterval(function(){show((cur+1)%EX.length);},7000);}

/* strona, która się buduje */
var site=$('#site'),webLoop=null;
if(site){var ring=$('#ring'),sc=$('#sc'),pop=$('#pop');
  webLoop=function(){site.classList.remove('done');pop.classList.remove('on');ring.style.transition='none';ring.setAttribute('stroke-dashoffset',100);sc.textContent='0';
    setTimeout(function(){site.classList.add('done');},1400);
    setTimeout(function(){ring.style.transition='stroke-dashoffset 1.4s cubic-bezier(.2,.8,.2,1)';ring.setAttribute('stroke-dashoffset',2);var t0=performance.now();(function c(t){var p=Math.min(1,(t-t0)/1400);sc.textContent=Math.round(98*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(c);})(t0);},2200);
    setTimeout(function(){pop.classList.add('on');},3600);};
  ring.setAttribute('stroke-dashoffset',2);sc.textContent='98';pop.classList.add('on');}

/* wykres */
var clr=$('#clr'),mkRun=null;
if(clr){clr.setAttribute('width',520);mkRun=function(){var t0=performance.now();(function c(t){var p=Math.min(1,(t-t0)/2200),e=1-Math.pow(1-p,3);clr.setAttribute('width',520*e);if(p<1)requestAnimationFrame(c);})(t0);};}

/* wejścia i start animacji przy widoczności */
var started={};
if('IntersectionObserver' in window){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var el=e.target;el.classList.remove('pre');
    if(el.classList.contains('dev')&&webLoop&&!started.w&&!red){started.w=1;webLoop();setInterval(webLoop,7000);}
    if(el.classList.contains('chart')&&mkRun&&!started.m&&!red){started.m=1;mkRun();}
    io.unobserve(el);});},{threshold:.15});
  $$('.rv').forEach(function(el){if(!red&&el.getBoundingClientRect().top>innerHeight)el.classList.add('pre');io.observe(el);});}

/* manifest */
var man=$('#man');
if(man){var gold=(man.getAttribute('data-gold')||'').split('|');man.innerHTML=man.textContent.trim().split(/\s+/).map(function(w){return '<span class="w'+(gold.indexOf(w)>=0?' gw':'')+'">'+w+'</span>';}).join(' ');
  var ws=$$('.w',man);var mu=function(){var b=man.getBoundingClientRect(),p=(innerHeight*.85-b.top)/(b.height+innerHeight*.35);p=Math.max(0,Math.min(1,p));var n=Math.round(p*ws.length);ws.forEach(function(w,i){w.classList.toggle('on',red||i<n);});};
  addEventListener('scroll',mu,{passive:true});mu();}

/* linia procesu */
$$('.steps').forEach(function(st){var u=function(){var b=st.getBoundingClientRect(),p=(innerHeight*.8-b.top)/(b.height+innerHeight*.3);st.style.setProperty('--p',Math.max(0,Math.min(1,red?1:p))*100+'%');};addEventListener('scroll',u,{passive:true});u();});

/* światło za kursorem */
$$('.tilt').forEach(function(c){c.addEventListener('pointermove',function(e){var b=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-b.left)/b.width*100+'%');c.style.setProperty('--my',(e.clientY-b.top)/b.height*100+'%');});});

/* przyciski magnetyczne */
if(!red&&matchMedia('(pointer:fine)').matches)$$('.mag').forEach(function(b){b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.transform='translate('+((e.clientX-r.left-r.width/2)*.16)+'px,'+((e.clientY-r.top-r.height/2)*.28)+'px)';});b.addEventListener('pointerleave',function(){b.style.transform='';});});

/* kalkulator w cenniku */
var calc=$('#calc');
if(calc){var out=$('#calc-v'),lst=$('#calc-l');
  var upd=function(){var sum=0,mo=0,items=[];$$('input[type=checkbox]',calc).forEach(function(c){if(c.checked){var v=+c.getAttribute('data-v');if(c.getAttribute('data-m'))mo+=v;else sum+=v;items.push(c.getAttribute('data-n'));}});
    out.textContent=(sum||mo)?('od '+(sum?sum.toLocaleString('pl-PL')+' zł':'')+(sum&&mo?' + ':'')+(mo?mo.toLocaleString('pl-PL')+' zł/mc':'')):'—';
    lst.innerHTML=items.length?items.map(function(x){return '<li>'+x+'</li>';}).join(''):'<li>Zaznacz, czego potrzebujesz</li>';};
  calc.addEventListener('change',upd);upd();}

/* formularze (podgląd) */
$$('form.f').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var req=$$('[required]',f).filter(function(i){return !i.value.trim();});if(req.length){req[0].focus();return;}
  [].forEach.call(f.children,function(x){if(!x.classList.contains('done'))x.style.display='none';});$('.done',f).style.display='block';});});
})();
/* hero automatyzacji: kroki zapalają się po kolei */
(function(){var rows=[].slice.call(document.querySelectorAll('.auto-vis .r'));if(!rows.length)return;
 var red=matchMedia('(prefers-reduced-motion: reduce)').matches,i=0;
 if(red){rows.forEach(function(r){r.classList.add('on');});return;}
 rows.forEach(function(r){r.classList.add('on');});
 setTimeout(function(){setInterval(function(){if(i===0)rows.forEach(function(r){r.classList.remove('on');});rows[i].classList.add('on');i=(i+1)%rows.length;},1100);},1500);})();
/* zawsze od góry strony po przejściu (bez #kotwicy) */
(function(){try{if('scrollRestoration' in history)history.scrollRestoration='manual';}catch(e){}
 function top(){if(!location.hash)window.scrollTo(0,0);}
 top();addEventListener('load',top);addEventListener('pageshow',top);setTimeout(top,80);
 var here=(location.pathname.split('/').pop()||'index.html');
 [].forEach.call(document.querySelectorAll('a.logo'),function(a){a.addEventListener('click',function(e){if(here==='index.html'||here===''){e.preventDefault();window.scrollTo({top:0,behavior:'smooth'});}});});
 [].forEach.call(document.querySelectorAll('.vplayer'),function(p){var v=p.querySelector('video'),b=p.querySelector('.ov');if(!v||!b)return;
  b.addEventListener('click',function(){p.classList.add('playing');v.controls=true;var pr=v.play();if(pr&&pr.catch)pr.catch(function(){});});
  v.addEventListener('ended',function(){p.classList.remove('playing');});});})();
/* rezerwacja konsultacji */
(function(){var days=document.getElementById('days');if(!days)return;
 var slotsEl=document.getElementById('slots'),sum=document.getElementById('bsum'),form=document.getElementById('bform'),done=document.getElementById('bdone');
 var DN=['nd','pon','wt','śr','czw','pt','sob'],MN=['sty','lut','mar','kwi','maj','cze','lip','sie','wrz','paź','lis','gru'],MF=['stycznia','lutego','marca','kwietnia','maja','czerwca','lipca','sierpnia','września','października','listopada','grudnia'];
 var DF=['niedziela','poniedziałek','wtorek','środa','czwartek','piątek','sobota'];
 var now=new Date(),list=[],d=new Date(now.getFullYear(),now.getMonth(),now.getDate());
 while(list.length<10){if(d.getDay()>0&&d.getDay()<6)list.push(new Date(d));d.setDate(d.getDate()+1);}
 var selD=null,selT=null;
 function paintSum(){if(selD&&selT){sum.innerHTML='Wybrany termin: <b>'+DF[selD.getDay()]+', '+selD.getDate()+' '+MF[selD.getMonth()]+', godz. '+selT+'</b>';document.getElementById('st2').classList.add('ok');}else sum.textContent='Najpierw wybierz dzień i godzinę.';}
 function slots(){slotsEl.innerHTML='';for(var h=9;h<17;h++)for(var m=0;m<60;m+=30){var t=h+':'+(m?'30':'00');var b=document.createElement('button');b.type='button';b.className='slot';b.textContent=t;
   var past=selD.toDateString()===now.toDateString()&&(h*60+m)<(now.getHours()*60+now.getMinutes()+60);if(past)b.disabled=true;
   (function(t,b){b.onclick=function(){selT=t;[].forEach.call(slotsEl.children,function(x){x.classList.remove('on');});b.classList.add('on');paintSum();};})(t,b);slotsEl.appendChild(b);}}
 list.forEach(function(x,i){var b=document.createElement('button');b.type='button';b.className='day';b.innerHTML='<small>'+DN[x.getDay()]+'</small><b>'+x.getDate()+'</b><span>'+MN[x.getMonth()]+'</span>';
   b.onclick=function(){selD=x;selT=null;[].forEach.call(days.children,function(y){y.classList.remove('on');});b.classList.add('on');document.getElementById('st1').classList.add('ok');slots();paintSum();};days.appendChild(b);
   if(i===0&&now.getHours()>=16){}});
 days.children[(now.getHours()>=16&&list[0].toDateString()===now.toDateString())?1:0].click();
 form.addEventListener('submit',function(e){e.preventDefault();if(!selD||!selT){sum.innerHTML='<b>Wybierz dzień i godzinę po lewej.</b>';return;}
  var req=[].filter.call(form.querySelectorAll('[required]'),function(i){return !i.value.trim();});if(req.length){req[0].focus();return;}
  form.style.display='none';done.style.display='block';document.getElementById('bdt').textContent=DF[selD.getDay()]+', '+selD.getDate()+' '+MF[selD.getMonth()]+', godz. '+selT;});
})();
/* kalendarz miesięczny */
(function(){var cal=document.getElementById('cal');if(!cal)return;
 var MF=['styczeń','luty','marzec','kwiecień','maj','czerwiec','lipiec','sierpień','wrzesień','październik','listopad','grudzień'],MG=['stycznia','lutego','marca','kwietnia','maja','czerwca','lipca','sierpnia','września','października','listopada','grudnia'],DF=['niedziela','poniedziałek','wtorek','środa','czwartek','piątek','sobota'];
 var now=new Date(),today=new Date(now.getFullYear(),now.getMonth(),now.getDate()),max=new Date(today);max.setDate(max.getDate()+60);
 var view=new Date(today.getFullYear(),today.getMonth(),1),selD=null,selT=null;
 var API='https://panel.elok-agency.pl/strona/',LIVE=/(^|\.)elok-agency\.pl$/.test(location.hostname),BUSY={},OFF={};
 function p2(n){return (n<10?'0':'')+n;} function ymd(d){return d.getFullYear()+'-'+p2(d.getMonth()+1)+'-'+p2(d.getDate());}
 var grid=document.getElementById('cgrid'),lab=document.getElementById('clab'),prev=document.getElementById('cprev'),next=document.getElementById('cnext'),slotsEl=document.getElementById('slots'),sd=document.getElementById('slotdate'),sum=document.getElementById('bsum'),form=document.getElementById('bform'),done=document.getElementById('bdone');
 function fmt(d){return DF[d.getDay()]+', '+d.getDate()+' '+MG[d.getMonth()];}
 function ok(d){var w=d.getDay();if(w===0||w===6||d<today||d>max||OFF[ymd(d)])return false;if(d.getTime()===today.getTime()&&now.getHours()>=15)return false;return true;}
 function paintSum(){if(selD&&selT){sum.innerHTML='Twój termin: <b>'+fmt(selD)+', godz. '+selT+'</b>';}else sum.textContent='Wybierz dzień w kalendarzu i godzinę.';}
 function slots(){slotsEl.innerHTML='';if(!selD){sd.textContent='Najpierw wybierz dzień w kalendarzu.';return;}sd.innerHTML='Wolne godziny: <b>'+fmt(selD)+'</b>';
  for(var h=9;h<17;h++)for(var m=0;m<60;m+=30){var t=h+':'+(m?'30':'00'),b=document.createElement('button');b.type='button';b.className='slot';b.textContent=t;
   if(selD.getTime()===today.getTime()&&(h*60+m)<(now.getHours()*60+now.getMinutes()+60))b.disabled=true;
   if(BUSY[ymd(selD)+' '+t]){b.disabled=true;b.classList.add('busy');b.title='Termin zajęty';}
   (function(t,b){b.onclick=function(){selT=t;[].forEach.call(slotsEl.children,function(x){x.classList.remove('on');});b.classList.add('on');document.getElementById('st2').classList.add('ok');paintSum();if(innerWidth<900){var f=document.getElementById('bsum');if(f)window.scrollTo({top:f.getBoundingClientRect().top+scrollY-100,behavior:'smooth'});}else{var n=document.getElementById('b-imie');if(n)n.focus({preventScroll:true});}};})(t,b);slotsEl.appendChild(b);}}
 function render(){lab.textContent=MF[view.getMonth()]+' '+view.getFullYear();grid.innerHTML='';
  var first=(view.getDay()+6)%7,days=new Date(view.getFullYear(),view.getMonth()+1,0).getDate();
  for(var i=0;i<first;i++)grid.appendChild(document.createElement('i'));
  for(var d=1;d<=days;d++){var dt=new Date(view.getFullYear(),view.getMonth(),d),b=document.createElement('button');b.type='button';b.textContent=d;
   if(dt.getTime()===today.getTime())b.classList.add('today');
   if(!ok(dt))b.disabled=true;else (function(dt,b){b.onclick=function(){selD=dt;selT=null;render();document.getElementById('st1').classList.add('ok');slots();paintSum();var s2=document.getElementById('st2');if(s2){var y=s2.getBoundingClientRect().top+scrollY-100;window.scrollTo({top:y,behavior:'smooth'});}};})(dt,b);
   if(selD&&dt.getTime()===selD.getTime())b.classList.add('on');
   b.setAttribute('aria-label',fmt(dt));grid.appendChild(b);}
  prev.disabled=view<=new Date(today.getFullYear(),today.getMonth(),1);next.disabled=new Date(view.getFullYear(),view.getMonth()+1,1)>max;}
 prev.onclick=function(){view=new Date(view.getFullYear(),view.getMonth()-1,1);render();};
 next.onclick=function(){view=new Date(view.getFullYear(),view.getMonth()+1,1);render();};
 render();slots();paintSum();
 function loadBusy(cb){if(!LIVE){if(cb)cb();return;}var x=new XMLHttpRequest();x.open('GET',API+'?a=zajete&_='+Date.now());x.timeout=8000;
  x.onload=function(){try{var r=JSON.parse(x.responseText);BUSY={};OFF={};(r.zajete||[]).forEach(function(k){BUSY[k]=1;});(r.wolne_dni||[]).forEach(function(k){OFF[k]=1;});
   if(selD&&!ok(selD)){selD=null;selT=null;}render();slots();paintSum();}catch(e){}if(cb)cb();};x.onerror=x.ontimeout=function(){if(cb)cb();};x.send();}
 loadBusy();
 var err=document.getElementById('berr'),btn=form.querySelector('button[type=submit]'),t0=Math.floor(Date.now()/1000);
 function showErr(m){if(!err)return;err.innerHTML=m;err.hidden=false;}
 function finish(){form.style.display='none';done.style.display='block';document.getElementById('bdt').textContent=fmt(selD)+', godz. '+selT;
  var y=done.getBoundingClientRect().top+scrollY-120;window.scrollTo({top:y,behavior:'smooth'});}
 form.addEventListener('submit',function(e){e.preventDefault();if(err)err.hidden=true;if(!selD||!selT){sum.innerHTML='<b>Wybierz dzień i godzinę w kalendarzu.</b>';return;}
  var req=[].filter.call(form.querySelectorAll('[required]'),function(i){return !i.value.trim();});if(req.length){req[0].focus();return;}
  var em=document.getElementById('b-mail');if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em.value.trim())){showErr('Sprawdź adres e-mail.');em.focus();return;}
  if(!LIVE){finish();return;}
  var v=function(id){var el=document.getElementById(id);return el?el.value.trim():'';};
  var data={a:'rezerwuj',imie:v('b-imie'),email:v('b-mail'),telefon:v('b-tel'),opis:v('b-opis'),data:ymd(selD),godz:selT,www2:v('b-www2'),ts:t0};
  var body=Object.keys(data).map(function(k){return encodeURIComponent(k)+'='+encodeURIComponent(data[k]);}).join('&');
  var old=btn.innerHTML;btn.disabled=true;btn.innerHTML='Wysyłam…';
  var x=new XMLHttpRequest();x.open('POST',API);x.setRequestHeader('Content-Type','application/x-www-form-urlencoded');x.timeout=20000;
  var fail=function(m){btn.disabled=false;btn.innerHTML=old;showErr(m||'Nie udało się wysłać. Spróbuj jeszcze raz albo zadzwoń: <a href="tel:+48455505820">455 505 820</a>.');};
  x.onload=function(){var r=null;try{r=JSON.parse(x.responseText);}catch(e){}
   if(r&&r.ok){finish();try{if(window.elokEv)elokEv('rezerwacja');if(window.elokKonwersja)elokKonwersja();}catch(e){}return;}
   if(x.status===409){selT=null;loadBusy();}
   fail(r&&r.error?r.error:null);};
  x.onerror=x.ontimeout=function(){fail();};x.send(body);});
})();
/* kopiowanie danych kontaktowych */
[].forEach.call(document.querySelectorAll('[data-copy]'),function(b){b.addEventListener('click',function(){var t=b.getAttribute('data-copy'),old=b.innerHTML;
 var fin=function(){b.innerHTML='<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'+' Skopiowano';b.classList.add('copied');setTimeout(function(){b.innerHTML=old;b.classList.remove('copied');},1800);};
 try{navigator.clipboard.writeText(t).then(fin,function(){});}catch(e){}});});
/* animacja: strona buduje się, klient wysyła zapytanie, telefon dostaje powiadomienie */
(function(){var wa=document.getElementById('wa');if(!wa)return;
 var red=matchMedia('(prefers-reduced-motion: reduce)').matches;
 var pg=wa.querySelector('.pg'),vp=wa.querySelector('.vp'),sk=wa.querySelector('.sk'),cur=wa.querySelector('.cur'),nt=wa.querySelector('.nt'),go=wa.querySelector('.go'),ring=wa.querySelector('#wring'),sc=wa.querySelector('#wsc');
 var fi=wa.querySelectorAll('.in'),TX=['Marek Kowalski','600 123 456'],PH=['Imię i nazwisko','Telefon'];
 var clk=wa.querySelector('.clk');
 function cl(x){return Math.max(0,Math.min(1,x));}
 function ez(x){x=cl(x);return 1-Math.pow(1-x,3);}
 function eio(x){x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;}
 function rel(el){var a=el.getBoundingClientRect(),b=wa.getBoundingClientRect();return {x:a.left-b.left,y:a.top-b.top,w:a.width,h:a.height};}
 var L=10.5,t0=performance.now(),vis=true;
 function state(t){
  sk.style.opacity=1-ez((t-1.0)/0.5);
  var fm=wa.querySelector('.fm'),maxS=Math.max(0,fm.offsetTop+fm.offsetHeight-vp.clientHeight+12);
  var s=eio((t-2.2)/1.1)*(1-eio((t-9.4)/0.8));pg.style.transform='translateY('+(-maxS*s)+'px)';
  for(var i=0;i<2;i++){var st=4.0+i*1.3,n=Math.floor(cl((t-st)/0.9)*TX[i].length);fi[i].textContent=n?TX[i].slice(0,n):PH[i];fi[i].classList.toggle('ph',!n);}
  var clicked=t>6.9&&t<9.6;go.classList.toggle('ok',clicked);go.innerHTML=clicked?'<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'+' Wysłano':'Zamów wycenę →';
  var p0=rel(fi[0]),p1=rel(fi[1]),p2=rel(go),start={x:wa.clientWidth*.55,y:wa.clientHeight*.95};
  var pts=[[3.4,start],[3.9,{x:p0.x+p0.w*.3,y:p0.y+p0.h*.6}],[5.2,{x:p1.x+p1.w*.3,y:p1.y+p1.h*.6}],[6.7,{x:p2.x+p2.w*.5,y:p2.y+p2.h*.6}]],cx=start.x,cy=start.y;
  for(var k=0;k<pts.length-1;k++){if(t>=pts[k][0]){var q=eio((t-pts[k][0])/((pts[k+1][0]-pts[k][0])*.8));cx=pts[k][1].x+(pts[k+1][1].x-pts[k][1].x)*q;cy=pts[k][1].y+(pts[k+1][1].y-pts[k][1].y)*q;}}
  if(t>=6.7){cx=pts[3][1].x;cy=pts[3][1].y;}
  cur.style.opacity=(t>3.3&&t<8.6)?1:0;cur.style.transform='translate('+cx+'px,'+cy+'px) scale('+(t>6.75&&t<6.95?.85:1)+')';
  var n=ez((t-7.3)/0.5)*(1-ez((t-10)/0.4));nt.style.opacity=n;nt.style.transform='translateY('+((1-n)*-14)+'px)';
  var r=ez((t-1.6)/1.4);if(ring){ring.setAttribute('stroke-dashoffset',100-98*r);sc.textContent=Math.round(98*r);}
 }
 function tick(now){if(vis){var t=((now-t0)/1000)%L;state(t);}requestAnimationFrame(tick);}
 var d=new Date();if(clk)clk.textContent=String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0');
 if(red){state(8.5);return;}
 if('IntersectionObserver' in window){new IntersectionObserver(function(es){vis=es[0].isIntersecting;},{threshold:.1}).observe(wa);}
 requestAnimationFrame(tick);})();
/* filmy w telefonie: włącz dźwięk */
[].forEach.call(document.querySelectorAll('.phonevid'),function(p){var v=p.querySelector('video'),b=p.querySelector('.snd');if(!v||!b)return;
 b.addEventListener('click',function(){if(v.muted){v.muted=false;v.currentTime=0;var pr=v.play();if(pr&&pr.catch)pr.catch(function(){});b.innerHTML='<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5L6 9H3v6h3l5 4z"/><path d="M22 9l-6 6M16 9l6 6"/></svg>'+'Wycisz';}else{v.muted=true;b.innerHTML='<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5L6 9H3v6h3l5 4z"/><path d="M15.5 8.5a5 5 0 010 7M18.5 5.5a9 9 0 010 13"/></svg>'+'Włącz dźwięk';}});});

/* animacja strony v2 */
(function(){var wb=document.getElementById('wb');if(!wb)return;var red=matchMedia('(prefers-reduced-motion: reduce)').matches;
 var sk=wb.querySelector('.sk'),cur=wb.querySelector('.cur'),nt=wb.querySelector('.nt'),go=wb.querySelector('.go'),ring=wb.querySelector('#wring'),sc=wb.querySelector('#wsc'),fi=wb.querySelectorAll('.in'),clk=wb.querySelector('.clk');
 var TX=['Marek Kowalski','600 123 456'],PH=['Imię i nazwisko','Telefon'],CK='<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg>';
 function cl(x){return Math.max(0,Math.min(1,x));}function ez(x){x=cl(x);return 1-Math.pow(1-x,3);}function eio(x){x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;}
 function rel(el){var a=el.getBoundingClientRect(),b=wb.getBoundingClientRect();return {x:a.left-b.left,y:a.top-b.top,w:a.width,h:a.height};}
 var L=9,t0=performance.now(),vis=true,last=-1;
 function state(t){sk.style.opacity=1-ez((t-0.9)/0.5);
  for(var i=0;i<2;i++){var st=2.4+i*1.3,n=Math.floor(cl((t-st)/0.9)*TX[i].length);fi[i].textContent=n?TX[i].slice(0,n):PH[i];fi[i].classList.toggle('pl',!n);}
  var clicked=t>5.2&&t<8.6,k=clicked?1:0;if(k!==last){go.innerHTML=clicked?CK+' Wysłano':'Wyślij zapytanie';last=k;}go.classList.toggle('ok',clicked);
  var p0=rel(fi[0]),p1=rel(fi[1]),p2=rel(go),s0={x:wb.clientWidth*.3,y:wb.clientHeight*.9};
  var P=[[1.7,s0],[2.2,{x:p0.x+p0.w*.35,y:p0.y+p0.h*.55}],[3.5,{x:p1.x+p1.w*.35,y:p1.y+p1.h*.55}],[5.0,{x:p2.x+p2.w*.5,y:p2.y+p2.h*.55}]],x=s0.x,y=s0.y;
  for(var j=0;j<P.length-1;j++){if(t>=P[j][0]){var q=eio((t-P[j][0])/((P[j+1][0]-P[j][0])*.8));x=P[j][1].x+(P[j+1][1].x-P[j][1].x)*q;y=P[j][1].y+(P[j+1][1].y-P[j][1].y)*q;}}
  if(t>=5.0){x=P[3][1].x;y=P[3][1].y;}
  cur.style.opacity=(t>1.6&&t<7)?1:0;cur.style.transform='translate('+x+'px,'+y+'px) scale('+(t>5.05&&t<5.25?.85:1)+')';
  var n2=ez((t-5.6)/0.5)*(1-ez((t-8.5)/0.4));nt.style.opacity=n2;nt.style.transform='translateY('+((1-n2)*-12)+'px)';
  var r=ez((t-1.2)/1.4);ring.setAttribute('stroke-dashoffset',100-98*r);sc.textContent=Math.round(98*r);}
 var d=new Date();clk.textContent=String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0');
 if(red){state(7);return;}
 if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting;},{threshold:.1}).observe(wb);
 (function tick(now){if(vis)state(((now-t0)/1000)%L);requestAnimationFrame(tick);})(t0);})();
/* filtr case studies */
(function(){var f=document.getElementById('cfil');if(!f)return;[].forEach.call(f.querySelectorAll('button'),function(b){b.addEventListener('click',function(){var c=b.getAttribute('data-c');
 [].forEach.call(f.querySelectorAll('button'),function(x){x.classList.toggle('on',x===b);});[].forEach.call(document.querySelectorAll('.ct'),function(ct){ct.hidden=!(c==='all'||(ct.getAttribute('data-c')||'').indexOf(c)>=0);});});});})();
/* do góry */
[].forEach.call(document.querySelectorAll('.totop'),function(b){b.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});});
/* ===== własne statystyki (bez cookies, bez IP) -> panel ===== */
(function(){var EP='https://panel.elok-agency.pl/strona/?a=ev';
 if(!/(^|\.)elok-agency\.pl$/.test(location.hostname))return;
 var q=location.search;
 try{if(/[?&]nielicz=1/.test(q))localStorage.setItem('elok_ja','1');if(/[?&]nielicz=0/.test(q))localStorage.removeItem('elok_ja');if(localStorage.getItem('elok_ja')==='1'){window.elokEv=function(){};return;}}catch(e){}
 function ss(k,v){try{if(v===undefined)return sessionStorage.getItem(k);sessionStorage.setItem(k,v);}catch(e){return null;}}
 var sid=ss('elok_sid');if(!sid){sid=Math.random().toString(36).slice(2)+Date.now().toString(36);ss('elok_sid',sid);}
 function par(n){var m=new RegExp('[?&]'+n+'=([^&#]*)').exec(q);return m?decodeURIComponent(m[1].replace(/\+/g,' ')).slice(0,80):'';}
 var src=ss('elok_src');
 if(!src){var s=par('utm_source'),md=par('utm_medium'),cp=par('utm_campaign');
  if(!s){if(par('fbclid'))s='facebook';else if(par('gclid')||par('gbraid')||par('wbraid'))s='google',md=md||'cpc';else if(par('ttclid'))s='tiktok';}
  var r='';try{r=document.referrer?new URL(document.referrer).hostname:'';}catch(e){}
  if(/elok-agency\.pl$/.test(r))r='';
  src=JSON.stringify({s:s,m:md,c:cp,r:r,l:location.pathname});ss('elok_src',src);}
 var S={};try{S=JSON.parse(src)||{};}catch(e){}
 var dev=innerWidth<700?'telefon':(innerWidth<1100?'tablet':'komputer');
 function send(ev,x){var d={ev:ev,p:location.pathname,sid:sid,s:S.s||'',m:S.m||'',c:S.c||'',r:S.r||'',l:S.l||'',d:dev,x:x||''};
  var b=Object.keys(d).map(function(k){return encodeURIComponent(k)+'='+encodeURIComponent(d[k]);}).join('&');
  try{if(navigator.sendBeacon&&navigator.sendBeacon(EP,new Blob([b],{type:'application/x-www-form-urlencoded'})))return;}catch(e){}
  try{var x2=new XMLHttpRequest();x2.open('POST',EP);x2.setRequestHeader('Content-Type','application/x-www-form-urlencoded');x2.send(b);}catch(e){}}
 window.elokEv=send;
 send('wejscie');
 document.addEventListener('click',function(e){var a=e.target.closest?e.target.closest('a,button'):null;if(!a)return;var h=a.getAttribute('href')||'';
  if(h.indexOf('tel:')===0)send('telefon');else if(h.indexOf('mailto:')===0)send('mail');
  else if(/konsultacja\.html/.test(h))send('klik_konsultacja',(a.textContent||'').trim().slice(0,60));
  else if(/demo\.html/.test(h))send('demo');
  else if(a.hasAttribute('data-copy'))send('kopiuj',a.getAttribute('data-copy').indexOf('@')>0?'mail':'telefon');
  else if(/instagram\.com|tiktok\.com|facebook\.com/.test(h))send('social',h.replace(/^https?:\/\/(www\.)?/,'').split('/')[0]);},true);
 var mx=0;addEventListener('scroll',function(){var p=Math.round((scrollY+innerHeight)/document.documentElement.scrollHeight*100);if(p>mx)mx=p;},{passive:true});
 var sent75=false;setInterval(function(){if(!sent75&&mx>=75){sent75=true;send('przewiniecie_75');}},3000);
})();
/* ===== statystyki i reklamy zewnętrzne (włączają się dopiero po zgodzie) =====
   Identyfikatory ustawiasz w panelu: panel.elok-agency.pl/strona/admin.php -> Podłączenia */
(function(){var C=window.ELOK_CFG||{},CFG={clarity:C.clarity||'',ga4:C.ga4||'',metaPixel:C.metaPixel||'',tiktokPixel:C.tiktokPixel||'',gads:C.gads||'',gadsLabel:C.gadsLabel||''};
 window.elokKonwersja=function(){try{if(window.fbq)fbq('track','Schedule');if(window.gtag){gtag('event','generate_lead');if(CFG.gads&&CFG.gadsLabel)gtag('event','conversion',{send_to:CFG.gads+'/'+CFG.gadsLabel});}if(window.ttq)ttq.track('SubmitForm');}catch(e){}};
 var any=CFG.clarity||CFG.ga4||CFG.metaPixel||CFG.tiktokPixel||CFG.gads;if(!any)return;
 function get(){try{return localStorage.getItem('elok_zgoda');}catch(e){return null;}}
 function set(v){try{localStorage.setItem('elok_zgoda',v);}catch(e){}}
 function js(src){var s=document.createElement('script');s.async=true;s.src=src;document.head.appendChild(s);}
 function load(){
  if(CFG.clarity){(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script",CFG.clarity);}
  if(CFG.ga4||CFG.gads){js('https://www.googletagmanager.com/gtag/js?id='+(CFG.ga4||CFG.gads));window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments);};gtag('js',new Date());if(CFG.ga4)gtag('config',CFG.ga4);if(CFG.gads)gtag('config',CFG.gads);}
  if(CFG.metaPixel){!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init',CFG.metaPixel);fbq('track','PageView');}
  if(CFG.tiktokPixel){!function(w,d,t){w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"];ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.load=function(e){var n="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{};ttq._i[e]=[];ttq._u=n;var o=d.createElement("script");o.async=!0;o.src=n+"?sdkid="+e+"&lib="+t;var a=d.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};ttq.load(CFG.tiktokPixel);ttq.page();}(window,document,'ttq');}
 }
 var z=get();if(z==='tak'){load();return;}if(z==='nie')return;
 var bar=document.createElement('div');bar.className='cookie';bar.setAttribute('role','dialog');bar.setAttribute('aria-label','Pliki cookies');
 bar.innerHTML='<p>Używamy plików cookies do statystyk i reklam. Możesz się zgodzić albo zostawić tylko niezbędne. <a href="cookies.html">Szczegóły</a></p><div><button type="button" class="btn sec" data-z="nie">Tylko niezbędne</button><button type="button" class="btn pri" data-z="tak">Akceptuję</button></div>';
 document.body.appendChild(bar);
 [].forEach.call(bar.querySelectorAll('button'),function(b){b.addEventListener('click',function(){var v=b.getAttribute('data-z');set(v);bar.remove();if(v==='tak')load();});});
})();
