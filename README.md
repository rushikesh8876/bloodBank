# Blood Bank Management System

**Live Demo:** [https://bloodbank-ju3c.onrender.com](https://bloodbank-ju3c.onrender.com)

---

## Default Login Credentials

### Admin Panel

- **URL:** [https://bloodbank-ju3c.onrender.com/admin/](https://bloodbank-ju3c.onrender.com/admin/)
- **Username:** admin
- **Email:** <admin@bloodbank.com>
- **Password:** bloodbank123

### Test User Login

- **Admin Login:** [https://bloodbank-ju3c.onrender.com/adminlogin](https://bloodbank-ju3c.onrender.com/adminlogin)
  - Username: admin
  - Password: bloodbank123

### Demo Accounts

You can also create your own donor and patient accounts through the respective signup pages:

- **Donor Signup:** [https://bloodbank-ju3c.onrender.com/donor/donorsignup](https://bloodbank-ju3c.onrender.com/donor/donorsignup)
- **Patient Signup:** [https://bloodbank-ju3c.onrender.com/patient/patientsignup](https://bloodbank-ju3c.onrender.com/patient/patientsignup)

---

## Screenshots

### Homepage

![homepage snap](https://github.com/sumitkumar1503/bloodbankmanagement/blob/master/static/screenshot/homepage.png?raw=true)

### Admin Dashboard

![dashboard snap](https://github.com/sumitkumar1503/bloodbankmanagement/blob/master/static/screenshot/admindashboard.png?raw=true)

### Blood Donation

![invoice snap](https://github.com/sumitkumar1503/bloodbankmanagement/blob/master/static/screenshot/blooddonation.png?raw=true)

### Blood Request

![doctor snap](https://github.com/sumitkumar1503/bloodbankmanagement/blob/master/static/screenshot/bloodrequest.png?raw=true)

### Logout

## ![doctor snap](https://github.com/sumitkumar1503/bloodbankmanagement/blob/master/static/screenshot/logout.png?raw=true)

## Functions

### Admin

- Admin account is automatically created during deployment
- After Login, can see Unit of blood of each blood group available, Number Of Donor, Number of blood request, Number of approved request, Total Unit of blood on Dashboard.
- Can View, Update, Delete Donor.
- Can View, Update, Delete Patient.
- Can View Donation Request made by donor and can approve or reject that request based on disease of donor.
- If Donation Request approved by admin then that unit of blood added to blood stock of that blood group.
- If Donation Request rejected by admin then 0 unit of blood added to stock.
- Can View Blood Request made by donor / patient and can approve or reject that request.
- If Blood Request approved by admin then that unit of blood reduced from blood stock of that blood group.
- If Blood Request rejected by admin then 0 unit of blood reduced from stock.
- Can see history of blood request.
- Can Update Unit Of Particular Blood Group.

### Donor

- Donor can create account by providing basic details.
- After Login, Donor can donate blood, After approval from admin only, blood will be added to blood stock.
- Donor can see their donation history with status (Pending, Approved, Rejected).
- Donor can also request for blood from blood stock.
- Donor can see their blood request history with status.
- Donor can see number of blood request Made, Approved, Pending, Rejected by Admin on their dashboard.

> **_NOTE:_** Donor can donate blood and can also request for blood.

### Patient

- Create account (No Approval Required By Admin, Can Login After Signup)
- After Login, Can see number of blood request Made, Approved, Pending, Rejected by Admin on their dashboard.
- Patient can request for blood of specific blood group and unit from blood stock.
- Patient can see their blood request history with status (Pending, Approved, Rejected).

---

## Deployment Information

This project is deployed on Render with the following configuration:

- **Platform:** Render (Free Tier)
- **Python Version:** 3.11.9
- **Database:** SQLite (for demo purposes)
- **Web Server:** Gunicorn

---

## HOW TO RUN THIS PROJECT LOCALLY

### Prerequisites

- Install Python (3.7.6 or higher)
- Git

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/rushikesh8876/bloodBank.git
cd bloodBank
```

2. **Install dependencies**

```bash
python -m pip install -r requirements.txt
```

3. **Run database migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create admin user (for local development)**

```bash
python manage.py createsuperuser
```

5. **Start the development server**

```bash
python manage.py runserver
```

6. **Access the application**

```
http://127.0.0.1:8000/
```

### Local Admin Access

After creating a superuser locally, you can access the admin panel at:

```
http://127.0.0.1:8000/admin/
```

---

## Technologies Used

- **Backend:** Django 4.2.16
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Deployment:** Render
- **Version Control:** Git/GitHub

---

## Project Structure

```
bloodbankmanagement/
├── blood/              # Blood management app
├── donor/              # Donor management app
├── patient/            # Patient management app
├── bloodbankmanagement/ # Main project settings
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version for deployment
├── Procfile           # Deployment configuration
└── manage.py          # Django management script
```
