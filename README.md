# django-moto-shop

**django-moto-shop** is a fully functional motorcycle e-commerce platform built with Django. Users can browse available motorcycles, filter them by brand, add products to a cart, register or log in, and place orders. The project includes both backend and frontend components and is containerized using Docker with monitoring and logging infrastructure.

---

## 🚀 Features

* 🛒 Shopping cart with session support
* 🧾 Order placement and checkout flow
* 🢍 Custom user model with GitHub OAuth support
* 📦 Product catalog with brand-based categorization
* 📊 REST API (Django REST Framework)
* 🚠 Admin panel with full management capabilities
* 💻 Frontend using HTML, CSS, Bootstrap, JavaScript (including jQuery)
* ✅ Phone number validation with JavaScript
* 🖼 Swiper integration on the homepage
* 📈 Monitoring with Prometheus, Grafana, Loki, and Promtail
* 📧 Yandex SMTP email support
* 🐳 Dockerized setup with Nginx and Docker Compose
* 📝 Logging and session management

---

## 💪 Technologies

* Python, Django, Django REST Framework
* PostgreSQL
* Docker, Docker Compose
* Nginx
* GitHub OAuth
* Prometheus, Grafana, Loki, Promtail
* Bootstrap, HTML/CSS, JavaScript, jQuery

---

## 📦 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-moto-shop.git
cd django-moto-shop
```

### 2. Create Environment Variables File

Copy the template and update it with your credentials:

```bash
cp .env.template .env
```

For more information on environment variables, see the `.env.template` file.

### 3. Start the Application

```bash
docker-compose up --build
```

The app will be accessible at:
📍 `http://localhost/`

---

## ⚙️ Initial Configuration

The `entrypoint.sh` script automatically performs:

* Applying database migrations
* Loading fixtures (if available)
* Creating a superuser (based on environment variables)

You can modify initial data in the `fixtures/` directory.

---

## 🔑 Authentication

* OAuth via GitHub
* Email/password registration and login
* Session-based authentication

---

## 🛁 API Access

A small REST API is available via Django REST Framework.

Visit:

```url
http://localhost/api/
```

---

## 👥 Admin Panel

Django Admin is available at:

```url
http://localhost/admin/
```

Login with the superuser credentials defined in your `.env`.

---

## 📊 Monitoring

This project includes the following monitoring services:

* **Prometheus** – metrics collection
* **Grafana** – data visualization (`http://localhost:3000`)
* **Loki + Promtail** – log aggregation

---

## 📄 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.

---

## ✍️ Author

Created by \[Neolog13]
GitHub repository: https://github.com/Neolog13/django-moto-shop
