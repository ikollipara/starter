/**------------------------------------------------------------
 * app.js
 * Ian Kollipara
 *
 * Main Entrypoint
 *------------------------------------------------------------**/

import "./scss/app.scss";
import * as Turbo from "@hotwired/turbo";
import { Application } from "@hotwired/stimulus";

/**
 * @typedef {Window & { Turbo: typeof import("@hotwired/turbo"), Stimulus: Application }} ExtWindow
 */

/** @type ExtWindow */
const win = window;

win.Turbo = Turbo;
win.Stimulus = Application.start();

// Register Controllers
