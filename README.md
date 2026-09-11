# Booking

**Booking** - це вебзастосунок на Django для пошуку та бронювання готельних номерів.

## Основні можливості

* **Пошук та каталог**: Гнучкий пошук готелів за назвою та містом, пагінація списку.
* **Управління готелями та номерами**: Повний CRUD для власників (створення, редагування, видалення готелів та кімнат).
* **Бронювання номерів**:
  * Перевірка доступності дат та запобігання перехресним/конфліктним бронюванням.
  * Автоматичний розрахунок вартості проживання.
  * Скасування бронювань.

## Технологічний стек

* **Backend**: Python 3.10+, Django 6.1
* **Frontend**: HTML5, CSS3, Bootstrap 5, Django Templates
* **Database**: SQLite

## Рольова модель

1. **Гість (`guest`)**:
   * Перегляд головної сторінки, каталогу та сторінок готелів.
   * Бронювання номерів.
   * Перегляд та скасування власних бронювань у профілі.
2. **Власник готелю (`owner`)**:
   * Усі можливості Гостя.
   * Створення та редагування власних готелів і номерів.
   * Перегляд списку всіх бронювань у своїх готелях.
3. **Адміністратор (`admin`)**:
   * Повний доступ до управління всіма сутностями проєкту через адмін-панель Django.

## Інструкція з розгортання та запуску

### 1. Клонування репозиторію
```bash
git clone https://github.com/Noi1-3/Booking.git
cd Booking
```

### 2. Створення та активація віртуального середовища

* **Windows:**

  ```bash
  python -m venv .venv
  .venv/Scripts/activate
  ```

* **macOS / Linux:**

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Встановлення залежностей
```bash
pip install -r requirements.txt
```

### 4. Застосування міграцій
```bash
python manage.py migrate
```

### 5. Створення суперкористувача
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера розробки
```bash
python manage.py runserver
```

### 7. Доступ до застосунку
Після запуску сервера перейдіть у браузері за адресою:
```text
http://127.0.0.1:8000/
```

## Карта шаблонів, представлень та форм

### 1. Загальні шаблони

| Файл шаблону | Призначення сторінки | Форма (Form) |
| :--- | :--- | :--- |
| `base.html` | Базовий каркас сторінок, підключення Bootstrap 5, метатегів, сповіщень та навігації | Відсутня |
| `includes/navbar.html` | Навігаційне меню з динамічними елементами залежно від ролі | POST-форма виходу |

### 2. Застосунок `users` (Авторизація та профілі)

| Файл шаблону | Призначення сторінки | Представлення (View) | Форма (Form) |
| :--- | :--- | :--- | :--- |
| `users/register.html` | Реєстрація нового користувача | `RegisterView` | `CustomUserCreationForm` |
| `users/login.html` | Авторизація користувача | `UserLoginView` | `CustomLoginForm` |
| `users/profile_detail.html` | Перегляд профілю користувача | `UserProfileDetailView` | Відсутня |
| `users/profile_update.html` | Редагування персональних даних | `UserProfileUpdateView` | `UserProfileForm` |
| `users/password_change.html` | Зміна пароля користувача | `UserPasswordChangeView` | `CustomPasswordChangeForm` |

### 3. Застосунок `hotels` (Готелі та номери)

| Файл шаблону | Призначення сторінки | Представлення (View) | Форма (Form) |
| :--- | :--- | :--- | :--- |
| `hotels/hotel_list.html` | Каталог готелів із фільтрацією та пагінацією | `HotelListView` | GET-форма пошуку (`title`, `city`) |
| `hotels/hotel_detail.html` | Детальна сторінка готелю та перелік номерів | `HotelDetailView` | Відсутня |
| `hotels/hotel_form.html` | Створення та редагування готелю | `HotelCreateView`, `HotelUpdateView` | `HotelForm` |
| `hotels/hotel_confirm_delete.html` | Підтвердження видалення готелю | `HotelDeleteView` | POST-форма підтвердження |
| `hotels/room_form.html` | Додавання та редагування кімнати | `RoomCreateView`, `RoomUpdateView` | `RoomForm` |
| `hotels/room_confirm_delete.html` | Підтвердження видалення кімнати | `RoomDeleteView` | POST-форма підтвердження |

### 4. Застосунок `bookings` (Бронювання)

| Файл шаблону | Призначення сторінки | Представлення (View) | Форма (Form) |
| :--- | :--- | :--- | :--- |
| `bookings/booking_form.html` | Вибір дат та оформлення бронювання | `BookingCreateView` | `BookingForm` |
| `bookings/booking_detail.html` | Детальна інформація про бронювання | `BookingDetailView` | Відсутня |
| `bookings/user_booking_list.html` | Список усіх бронювань поточного клієнта | `UserBookingListView` | Відсутня |
| `bookings/owner_booking_list.html` | Список усіх бронювань у готелях власника | `HotelOwnerBookingListView` | Відсутня |
| `bookings/booking_confirm_cancel.html` | Підтвердження скасування бронювання | `BookingCancelView` | POST-форма підтвердження |
