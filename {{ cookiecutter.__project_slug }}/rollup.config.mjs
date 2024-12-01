/**------------------------------------------------------------
 * rollup.config.mjs
 * {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
 *
 * Rollup Configuration
 *------------------------------------------------------------**/

import postcss from "rollup-plugin-postcss";
import { nodeResolve } from "@rollup/plugin-node-resolve";
import { defineConfig } from "rollup";

export default defineConfig({
  plugins: [nodeResolve(), postcss()],
  input: "static_src/app.mjs",
  output: {
    dir: "static",
  },
});
