# ============================================================
# SHOP INVENTORY MANAGEMENT SYSTEM - FLASK APPLICATION
# Combined TA-1 & TA-2 DSA Web Server
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from dsa import Item, ArrayInventory, SinglyLinkedList, DoublyLinkedList

app = Flask(__name__)

# Initialize our 3 core Data Structures
array_inventory = ArrayInventory()
singly_list = SinglyLinkedList()
doubly_list = DoublyLinkedList()


def seed_initial_inventory():
    """Pre-load sample shop items so the dashboard looks rich immediately."""
    sample_products = [
        (101, "Mechanical Keyboard", 2499.00, 14),
        (102, "Wireless Gaming Mouse", 1299.00, 22),
        (103, "USB-C Fast Hub 7-in-1", 1850.00, 9),
        (104, "27-inch IPS Monitor", 14500.00, 5),
    ]
    for item_id, name, price, qty in sample_products:
        array_inventory.add_item(Item(item_id, name, price, qty))
        singly_list.insert_at_end(Item(item_id, name, price, qty))
        doubly_list.insert_at_end(Item(item_id, name, price, qty))


seed_initial_inventory()


@app.route("/")
def home():
    items = singly_list.get_all()
    total_items = len(items)
    total_units = sum(i.qty for i in items)
    total_value = sum(i.qty * i.price for i in items)

    return render_template(
        "index.html",
        total_items=total_items,
        total_units=total_units,
        total_value=total_value
    )


@app.route("/add", methods=["GET", "POST"])
def add_item():
    message = None
    success = False

    if request.method == "POST":
        try:
            item_id = int(request.form.get("item_id"))
            name = request.form.get("name", "").strip()
            price = float(request.form.get("price"))
            qty = int(request.form.get("qty"))

            if singly_list.search(item_id) is not None:
                message = f"Item ID #{item_id} already exists in inventory!"
                success = False
            else:
                array_inventory.add_item(Item(item_id, name, price, qty))
                singly_list.insert_at_end(Item(item_id, name, price, qty))
                doubly_list.insert_at_end(Item(item_id, name, price, qty))

                message = f"Product '{name}' (ID #{item_id}) added to Array, Singly & Doubly Linked Lists!"
                success = True
        except ValueError:
            message = "Invalid input values. Please check ID, Price, and Quantity."
            success = False

    return render_template("add_item.html", message=message, success=success)


@app.route("/items")
def items():
    singly_items = singly_list.get_all()
    array_items = array_inventory.get_all()
    total_value = sum(i.qty * i.price for i in singly_items)

    return render_template(
        "items.html",
        items=singly_items,
        array_items=array_items,
        total_value=total_value
    )


@app.route("/update_qty/<int:item_id>", methods=["POST"])
def update_qty(item_id):
    delta = int(request.form.get("delta", 0))
    item = singly_list.search(item_id)
    if item is not None:
        new_qty = max(0, item.qty + delta)
        singly_list.update_qty(item_id, new_qty)
        array_inventory.update_qty(item_id, new_qty)
        doubly_list.update_qty(item_id, new_qty)
    return redirect(url_for("items"))


@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    singly_list.delete_by_id(item_id)
    array_inventory.delete_by_id(item_id)
    doubly_list.delete_by_id(item_id)
    return redirect(url_for("items"))


@app.route("/search", methods=["GET", "POST"])
def search_item():
    item = None
    message = None

    if request.method == "POST":
        try:
            item_id = int(request.form.get("item_id"))
            item = singly_list.search(item_id)
            if item is None:
                message = f"No product found with Item ID #{item_id}."
        except ValueError:
            message = "Please enter a valid numeric Item ID."

    return render_template("search.html", item=item, message=message)


@app.route("/doubly")
def doubly():
    forward = doubly_list.get_forward()
    backward = doubly_list.get_backward()
    return render_template("doubly.html", forward=forward, backward=backward)


if __name__ == "__main__":
    app.run(debug=True, port=5000)