# RoleProgress — Progress Atlas

A responsive, locally runnable concept website and isolated synthetic workforce-transition demo. The selected art direction combines ivory terrain, sage contours, copper paths, aubergine mountains, Newsreader display type and Manrope interface type.

## Run

```sh
npm install
npm run dev -- --port 4174
```

Open http://localhost:4174. If that port is occupied, Vite prints the next available port.

```sh
npm run build
npm run test:sites
```

The production frontend is emitted to `dist/client`. The bootstrap's hosting adapter remains intact. No remote deployment, repository, domain, payment processor or customer database has been created.

## Included

- Original RP logo, favicon and app icon; self-hosted fonts; custom generated terrain, mountain and workplace imagery.
- GSAP hero entrances, directional section reveals, staggered evidence/table rows, animated report bars, desktop pinned horizontal pathway, Lenis scrolling and footer parallax.
- Motion pause control; system reduced-motion setting initializes a static experience. Smaller screens use a vertical pathway. Decorative card previews are inert; actionable product links remain available.
- Five separate product pages: Skills Desk, Skills Review, Skills Proof, Skills Signal and Skills Report.
- Platform, features, pricing, company, contact, employer/partner/board/assessor solutions, logistics, future knowledge work, worker rights, trust, sources, outcomes, resources, privacy, terms and access preview.
- Demo cohort queue with ten fictional records, search/filter, evidence pane, worker correction, reviewer simulation, pathway canvas, training availability, employer commitment stages, report and illustrative CSV export.
- Employer/demo/contact forms with client validation and honest local-only confirmation.
- Editable pilot templates under `public/templates`, linked from the Resources pages.
- Actual browser captures at 1440px and 390px in `screenshots`; tablet inspected at 768px.

## Important scope

This is a research-stage concept, not production matching or hiring software. All employer, worker, provider, outcome and commitment records are invented. WN-024 is the detailed evidence example; the other nine records demonstrate queue states. Corrections and reviewer controls live in browser memory; a reload resets them. Forms send nothing and store nothing. Authentication, HRIS/LMS imports, marketing analytics, enrollment, credential issuance and payments are not connected.

The $4,000 / 25-person cohort design is a test hypothesis, not accepted pricing. There are no customers, verified results, real interview slots, security certifications, job guarantees or precise worker fit scores claimed.

O*NET role IDs are linked as candidate occupational context. The O*NET database release and ESCO URI mapping remain explicitly pending. A real service needs version/license review, mapping validation, valid assessments, live provider availability, employer interview commitment and appropriate consent/procurement review.

## Main source files

- `src/App.jsx`: routing, Lenis/GSAP lifecycle, motion controls and correction state.
- `src/Home.jsx`: homepage chapters.
- `src/ui.jsx`: navigation, footer, product visuals and evidence components.
- `src/Pages.jsx`: product, company, resource, inquiry and access pages.
- `src/Demo.jsx`: synthetic workspace and correction modal.
- `src/content.js`: module/page copy and consistent fixtures.
- `src/ResourceKit.jsx`: downloadable materials and research references.
- `src/styles.css`: brand tokens, layout, interactions and responsive behavior.

## Asset provenance

Landscape and workplace illustrations/photos were generated specifically for this concept and are labeled illustrative where appropriate. These are not customer or employee photographs. Original PNGs are retained; the site serves optimized WebP assets (about 637 KB total for the four large images). The RP mark was generated for the project. Phosphor provides the interface icon family. Font packages include their licenses.

## Validation

Production build and all four existing hosting-adapter tests passed. Browser checks covered desktop/mobile navigation, cohort search, correction submission and retained statement, reviewer feedback, course expansion, form validation/success visibility, horizontal scrolling, skip navigation, motion pause, tablet layout and overflow. See `design-qa.md` for visual comparisons, resolved findings and remaining launch limitations.

## Current identity update
Option 3 Progress Folio replaces the original RP monogram. `public/brand` contains 16 SVGs with outlined lettering and no embedded rasters, plus PNG/ICO favicons and app icons. `/brand/index.html` previews the set. The downloadable archive is `../RoleProgress-vector-brand-kit.zip`. The page palette now balances white with sage, lilac, muted copper and mist blue; cards remain straight.
