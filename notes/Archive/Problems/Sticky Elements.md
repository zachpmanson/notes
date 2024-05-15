---
tags:
  - nextjs
---
1. Pick element Child to be `position: sticky`.  Ensure it has a one of the following set: `top,bottom,left,right`
2. Ensure it has a parent that has `position: relative`
3. Ensure that all elements between the parent and child have `overflow: visible`
    - **Next.js sets `overflow:disabled` on the entire document by default**
    - **Many MUI elements will have `overflow: hidden` set, check all parents for this.**
    - Easiest to diagnose this by selecting child in Inspect Element, filter styles for "overflow" and click up repeatedly to traverse up the DOM.
