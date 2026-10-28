import {Resvg} from '@resvg/resvg-js';
import fs from 'node:fs';
for(const size of [16,32,48,180,192,512]){
 const input=fs.readFileSync('public/brand/'+(size<=48?'favicon.svg':'app-icon.svg'));
 const name=size===180?'apple-touch-icon.png':`icon-${size}.png`;
 fs.writeFileSync('public/brand/'+name,new Resvg(input,{fitTo:{mode:'width',value:size}}).render().asPng());
}
