from fastapi import FastAPI
import xmlrpc.client

app = FastAPI()

url = "http://localhost:8017"
db = "mydb"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
if not uid:
    raise Exception("Gagal login ke Odoo, cek DB/username/password!")

models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

@app.post("/sale/create")
def create_so(partner_id: int, order_lines: list):
    so_id = models.execute_kw(
        db, uid, password,
        "sale.order", "create",
        [{
            "partner_id": partner_id,
            "order_line": order_lines
        }]
    )
    return {"sale_id": so_id}


@app.put("/sale/{sale_id}")
def update_so(sale_id: int, values: dict):
    result = models.execute_kw(
        db, uid, password,
        "sale.order", "write",
        [[sale_id], values]
    )
    return {"success": result}


@app.get("/sale/list")
def list_so():
    so_list = models.execute_kw(
        db, uid, password,
        "sale.order", "search_read",
        [[]],
        {"fields": ["name", "partner_id", "state", "invoice_status"]}
    )
    return so_list


@app.get("/sale/{sale_id}")
def get_so_detail(sale_id: int):
    so_detail = models.execute_kw(
        db, uid, password,
        "sale.order", "read",
        [[sale_id]],
        {"fields": ["name", "partner_id", "state", "amount_total", "invoice_status"]}
    )
    return so_detail


@app.post("/sale/{sale_id}/confirm")
def confirm_so(sale_id: int):
    result = models.execute_kw(
        db, uid, password,
        "sale.order", "action_confirm",
        [[sale_id]]
    )
    return {"success": True if result else False}


@app.post("/sale/{sale_id}/cancel")
def cancel_so(sale_id: int):
    result = models.execute_kw(
        db, uid, password,
        "sale.order", "action_cancel",
        [[sale_id]]
    )
    return {"success": True if result else False}


@app.post("/sale/{sale_id}/reset")
def reset_so(sale_id: int):
    result = models.execute_kw(
        db, uid, password,
        "sale.order", "action_draft",
        [[sale_id]]
    )
    return {"success": True if result else False}