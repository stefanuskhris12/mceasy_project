/** @odoo-module **/

import { Component, mount } from "@odoo/owl";

export class ExternalInvoiceForm extends Component {}
ExternalInvoiceForm.template = "external_invoice_request.ExternalInvoiceForm";

document.addEventListener("DOMContentLoaded", () => {
    const target = document.querySelector("#external_invoice_form_root");
    if (target) {
        const saleOrders = JSON.parse(target.dataset.sale_orders || "[]");

        console.log(">>> Mounting ExternalInvoiceForm <<<", saleOrders);

        mount(ExternalInvoiceForm, {
            target,
            props: { saleOrders },
        });
    }
});
