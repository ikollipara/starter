/**------------------------------------------------------------
 * app.js
 * Ian Kollipara
 *
 * Main Entrypoint
 *------------------------------------------------------------**/

import "./scss/app.scss";
import * as Turbo from "@hotwired/turbo";
import { Application } from "@hotwired/stimulus";

window.Turbo = Turbo;
window.Stimulus = Application.start();

// Register Controllers
