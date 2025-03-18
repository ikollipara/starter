/**------------------------------------------------------------
 * rollup.config.mjs
 * {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
 *
 * Rollup Configuration
 *------------------------------------------------------------**/

import postcss from "rollup-plugin-postcss";
import { nodeResolve } from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import { defineConfig } from "rollup";

export default defineConfig({
  plugins: [
    commonjs(),
    nodeResolve({ browser: true }),
    postcss({ extensions: [".scss", ".sass", ".css"], extract: true }),
  ],
  input: "static/src/app.js",
  output: { dir: "static/dist" },
});
