/* @odoo-module  */
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class LoginPageAction extends Component {
    static template = "app_one.LoginPage";
}
registry.category("actions").add("app_one.action_login_page", LoginPageAction);