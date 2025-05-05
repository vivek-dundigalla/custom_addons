/** @odoo-module **/

import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
import { patch } from "@web/core/utils/patch";

patch(ReceiptScreen.prototype, {
    setup() {
        super.setup();
        this.receipt_template = 'sdm_pos_customization.ReceiptScreen';  // Must match t-name
    },
});
