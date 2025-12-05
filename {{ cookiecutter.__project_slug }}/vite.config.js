/**
* Name:          vite.config.js
* Author:	 Ian Kollipara <ian.kollipara@gmail.com>
* Created:	 2025-10-17
* Updated:	 2025-10-17
* Description: 
*  Vite Configuration File
*/


import { defineConfig } from "vite";
import { analyzer } from "vite-bundle-analyzer";
import * as path from "node:path";

export default defineConfig({
  plugins: [analyzer()],
  base: "/static/",
  build: {
    manifest: "manifest.json",
    outDir: path.resolve("./static/dist"),
    rollupOptions: {
      input: path.resolve("./static/src/app.js")
    }
  }
});
