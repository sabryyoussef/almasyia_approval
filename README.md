# almasyia_approval
Here's a `README.md` file tailored for your custom Odoo module `Almasyia_scc2`:

---

# 📄 Almasyia\_scc2 – Custom Odoo Approvals Module

A custom Odoo module designed to manage various types of approval requests in a structured workflow, integrating with HR, product, and sales modules.

## ✅ Features

* Request and track approvals for:

  * Business trips
  * Out-of-office entries
  * Overtime
  * Borrowing items
  * Procurements
  * Contracts
  * General-purpose approvals
* Configurable approval categories and workflows
* Multi-level approver support via next activities
* Integration with Odoo Sales and HR
* Fully integrated with Odoo's chatter and mail activity system

## 📦 Module Information

| Key          | Value                           |
| ------------ | ------------------------------- |
| Name         | Almasyia\_scc2                  |
| Version      | 1.0                             |
| Category     | Human Resources / Approvals     |
| Dependencies | `mail`, `hr`, `product`, `sale` |
| License      | OEEL-1                          |

## 📁 Contents

* **Security**

  * Role definitions and access controls
* **Data**

  * Default approval categories and mail activity types
* **Views**

  * Custom approval request forms
  * Category and product line management
  * Sales order and user views extensions
* **Demo Data**

  * Sample approval request entries for testing
* **Assets**

  * JavaScript models, components, and test helpers

## 🧩 Dependencies

Make sure the following core Odoo modules are installed:

* `mail`
* `hr`
* `product`
* `sale`

## 🚀 Installation

1. Clone the module into your Odoo `addons` directory:

   ```bash
   git clone https://github.com/yourusername/almasyia_scc2.git
   ```

2. Restart the Odoo server and update the app list:

   ```bash
   ./odoo-bin -u almasyia_scc2
   ```

3. Activate the developer mode in Odoo and install the **Almasyia\_scc2** module from the Apps menu.

## 🧪 Testing

Automated QUnit and tour tests are included under:

```
approvals/static/tests/
```

You can run these from the Odoo test suite interface or using test commands.

## 🔒 License

This module is licensed under the **Odoo Enterprise Edition License (OEEL-1)**.

## 🙌 Contributing

If you'd like to suggest improvements or contribute, feel free to fork the repository and submit a pull request.

---

sabry youssef
01000059085
egypt
