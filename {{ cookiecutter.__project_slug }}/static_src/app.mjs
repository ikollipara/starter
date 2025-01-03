/**------------------------------------------------------------
 * app.mjs
 * {{ cookiecutter.author_name }} <{{cookiecutter.author_email }}>
 *
 * Frontend Entrypoint
 *------------------------------------------------------------**/

import "./scss/app.scss";
import htmx from "htmx.org";
import { Application } from "@hotwired/stimulus";

window.htmx = htmx;
window.Stimulus = Application.start();
