/** @odoo-module */

import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"
import { loadJS } from "@web/core/assets"
const { Component, useState, onWillStart } = owl


export class Base extends Component {
    setup(){
        const notificationService = useService("notification");
        notificationService.add("Welcome !!!");
    }
}


Base.template = "owl_basic_app.TemplateName"
registry.category("actions").add("owl_basic_app.Base", Base)