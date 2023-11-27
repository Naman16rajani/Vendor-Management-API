# Vendor Management System API

Welcome to the Vendor Management System API. This API allows you to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/vendor-management.git
cd vendor-management
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The API will be accessible at http://127.0.0.1:8000/.

## API Reference

Vendor Endpoints

- Create a Vendor:

  - URL: POST /api/vendors/
  - Request Body:

  ```json
  {
    "name": "Vendor ABC",
    "contact_details": "Contact details here",
    "address": "Vendor address here",
    "vendor_code": "ABC123"
  }
  ```

- List All Vendors:

  - URL: GET /api/vendors/

- Retrieve a Specific Vendor:

  -URL: GET /api/vendors/{vendor_id}/

- Update a Vendor:

  - URL: PUT /api/vendors/{vendor_id}/
  - Request Body:

  ```json
  {
    "name": "Updated Vendor Name",
    "contact_details": "Updated contact details",
    "address": "Updated address",
    "vendor_code": "ABC123"
  }
  ```

- Delete a Vendor:
  - URL: DELETE /api/vendors/{vendor_id}/

Purchase Order Endpoints

- Create a Purchase Order:

  - URL: POST /api/purchase_orders/
  - Request Body:

  ```json
  {
     "po_number": "PO123",
      "vendor": 1,  # Use the actual primary key of the vendor
      "order_date": "2023-12-01T12:00:00Z",
      "delivery_date": "2023-12-15T12:00:00Z",
      "items": [{"item": "Product A", "quantity": 10}],
      "quantity": 10,
      "status": "pending"
  }
  ```

- List All Purchase Orders:
  - URL: GET /api/purchase_orders/
- Retrieve a Specific Purchase Order:
  - URL: GET /api/purchase_orders/{po_id}/
- Update a Purchase Order:

  - URL: PUT /api/purchase_orders/{po_id}/
  - Request Body:

  ```json
  {
    "status": "completed",
    "quality_rating": 4.5
  }
  ```

- Delete a Purchase Order:
  - URL: DELETE /api/purchase_orders/{po_id}/

Vendor Performance Endpoints

- Retrieve Vendor Performance Metrics:
  - URL: GET /api/vendors/{vendor_id}/performance/

Test Acknowledge Purchase Order Endpoint

- Acknowledge Purchase Order:
  - URL: PUT /api/purchase_orders/{po_id}/acknowledge/

## Authentication

Secure the API endpoints using token-based authentication.

goto URL: GET /api/getToken/

username: root

password: root

## Testing

Use tools like curl or Postman to test the API.
