import React,{useEffect,useRef,useState} from 'react';
export function Intro(){
 const video=useRef(null), left=useRef(false);
 const [ready,setReady]=useState(false),[blocked,setBlocked]=useState(false);
 const advance=()=>{if(left.current)return;left.current=true;window.dispatchEvent(new Event('roleprogress:hero'));};
 useEffect(()=>{const el=video.current;const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
 if(reduced){setBlocked(true);return;}
 el.play().catch(()=>setBlocked(true));
 const onScroll=()=>{if(window.scrollY>window.innerHeight*.65)left.current=true;};
 const observer=new MutationObserver(()=>{if(document.querySelector('.motion-paused'))el.pause();else if(!el.ended)el.play().catch(()=>setBlocked(true));});
 observer.observe(document.getElementById('top'),{attributes:true,attributeFilter:['class']});
 window.addEventListener('scroll',onScroll,{passive:true});return()=>{observer.disconnect();window.removeEventListener('scroll',onScroll);};},[]);
 return <section className={'cinema-intro '+(ready?'is-ready':'')} aria-label="RoleProgress introduction">
 <video ref={video} src="/assets/roleprogress-intro.mp4" muted playsInline preload="auto" onLoadedData={()=>setReady(true)} onEnded={advance} onError={()=>setBlocked(true)} aria-label="A copper pathway revealed through sculpted mountain terrain"/>
 <div className="cinema-copy"><span className="overline">ROLEPROGRESS · EVIDENCE FOR WHAT COMES NEXT</span><h2>Experience.<br/>Possibility.<br/><em>A path forward.</em></h2><p>Connect the skills people bring<br/>to the roles they could grow into.</p><button className="button" onClick={advance}>Discover the pathway <span aria-hidden="true">↓</span></button></div>
 <div className="cinema-bottom"><span>CONCEPT PREVIEW</span>{blocked?<button onClick={()=>{left.current=false;video.current.play().then(()=>setBlocked(false)).catch(()=>setBlocked(true));}}>Play introduction</button>:<button onClick={advance}>Skip introduction ↓</button>}</div>
 </section>;
}
