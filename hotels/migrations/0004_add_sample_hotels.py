from django.db import migrations


SAMPLE_HOTELS = (
    {
        'title': 'Львівська Кам’яниця',
        'city': 'Львів',
        'address': 'вул. Вірменська, 18',
        'description': 'Затишний бутик-готель у старовинній кам’яниці за кілька хвилин від площі Ринок. Сніданки, внутрішній дворик і тиха атмосфера.',
        'rooms': (('101', 2, '2450.00', True), ('203', 3, '3180.00', True), ('305', 2, '3900.00', False)),
    },
    {
        'title': 'Дніпровська Панорама',
        'city': 'Київ',
        'address': 'Набережне шосе, 9',
        'description': 'Сучасний міський готель із панорамним видом на Дніпро, просторими номерами, коворкінгом та рестораном української кухні.',
        'rooms': (('410', 2, '3290.00', True), ('512', 2, '3850.00', True), ('614', 4, '5200.00', True)),
    },
    {
        'title': 'Морський Бриз',
        'city': 'Одеса',
        'address': 'Французький бульвар, 42',
        'description': 'Курортний готель неподалік моря з терасою, зеленим садом і сімейними номерами. Підходить для спокійного літнього відпочинку.',
        'rooms': (('12', 2, '2750.00', True), ('18', 3, '3400.00', True), ('24', 4, '4650.00', False)),
    },
    {
        'title': 'Карпатська Тиша',
        'city': 'Яремче',
        'address': 'вул. Свободи, 156',
        'description': 'Гірський готель серед смерек із камінною залою, сауною та видом на Карпати. Поруч туристичні маршрути й водоспад Пробій.',
        'rooms': (('Шале 1', 2, '2900.00', True), ('Шале 2', 4, '4400.00', True), ('Люкс', 3, '5100.00', True)),
    },
    {
        'title': 'Буковинський Двір',
        'city': 'Чернівці',
        'address': 'вул. Ольги Кобилянської, 31',
        'description': 'Елегантний готель у центрі Чернівців з інтер’єрами, натхненими буковинською культурою, та домашніми сніданками.',
        'rooms': (('7', 1, '1650.00', True), ('11', 2, '2180.00', True), ('15', 3, '2850.00', True)),
    },
    {
        'title': 'Подільський Сад',
        'city': 'Кам’янець-Подільський',
        'address': 'вул. Старобульварна, 8',
        'description': 'Невеликий готель у Старому місті з краєвидом на фортецю, садом і терасою для вечірнього відпочинку.',
        'rooms': (('1', 2, '1950.00', True), ('4', 2, '2250.00', False), ('8', 4, '3600.00', True)),
    },
    {
        'title': 'Полтавська Садиба',
        'city': 'Полтава',
        'address': 'вул. Соборності, 27',
        'description': 'Комфортний готель у спокійній частині центру. Просторі кімнати, локальна кухня та зручний простір для сімейних поїздок.',
        'rooms': (('21', 2, '1750.00', True), ('22', 3, '2300.00', True)),
    },
    {
        'title': 'Харків Central',
        'city': 'Харків',
        'address': 'вул. Сумська, 54',
        'description': 'Функціональний готель для ділових і туристичних поїздок із цілодобовою рецепцією, швидким Wi-Fi та робочими зонами.',
        'rooms': (('301', 1, '1450.00', True), ('304', 2, '1890.00', True), ('307', 2, '2150.00', False)),
    },
    {
        'title': 'Ужгородський Замок',
        'city': 'Ужгород',
        'address': 'вул. Капітульна, 12',
        'description': 'Атмосферний мініготель біля замку з винним льохом, закарпатськими сніданками та номерами в теплих природних відтінках.',
        'rooms': (('A1', 2, '2250.00', True), ('A2', 2, '2550.00', True), ('B1', 3, '3100.00', True)),
    },
    {
        'title': 'Черкаси Riverside',
        'city': 'Черкаси',
        'address': 'вул. Героїв Дніпра, 81',
        'description': 'Світлий готель біля набережної з видом на воду, прокатом велосипедів та номерами для коротких і тривалих зупинок.',
        'rooms': (('6', 2, '1850.00', True), ('9', 4, '2950.00', True)),
    },
    {
        'title': 'Вінницька Резиденція',
        'city': 'Вінниця',
        'address': 'вул. Архітектора Артинова, 19',
        'description': 'Класичний міський готель поруч із центром і набережною Roshen. Є сімейні апартаменти та затишне кафе.',
        'rooms': (('202', 2, '2100.00', True), ('204', 3, '2780.00', True), ('206', 4, '3500.00', False)),
    },
    {
        'title': 'Тернопіль Lake Hotel',
        'city': 'Тернопіль',
        'address': 'вул. Білецька, 14',
        'description': 'Спокійний готель поблизу Тернопільського ставу з ранковими сніданками, лаунж-зоною та прогулянковими маршрутами поруч.',
        'rooms': (('33', 1, '1550.00', True), ('35', 2, '2050.00', True), ('37', 3, '2700.00', True)),
    },
)


def add_sample_hotels(apps, schema_editor):
    User = apps.get_model('users', 'User')
    Hotel = apps.get_model('hotels', 'Hotel')
    Room = apps.get_model('hotels', 'Room')

    owner, _ = User.objects.get_or_create(
        username='demo_hotel_owner',
        defaults={
            'email': 'hotels@example.com',
            'first_name': 'Демо',
            'last_name': 'Власник',
            'role': 'owner',
            'password': '!',
            'is_active': True,
        },
    )

    for data in SAMPLE_HOTELS:
        hotel, _ = Hotel.objects.get_or_create(
            title=data['title'],
            city=data['city'],
            defaults={
                'owner': owner,
                'address': data['address'],
                'description': data['description'],
            },
        )
        for number, capacity, price, is_available in data['rooms']:
            Room.objects.get_or_create(
                hotel=hotel,
                room_number=number,
                defaults={
                    'capacity': capacity,
                    'price_per_night': price,
                    'is_available': is_available,
                },
            )


def remove_sample_hotels(apps, schema_editor):
    User = apps.get_model('users', 'User')
    Hotel = apps.get_model('hotels', 'Hotel')

    titles = [hotel['title'] for hotel in SAMPLE_HOTELS]
    Hotel.objects.filter(
        owner__username='demo_hotel_owner',
        title__in=titles,
    ).delete()
    User.objects.filter(
        username='demo_hotel_owner',
        hotels__isnull=True,
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_room_capacity'),
    ]

    operations = [
        migrations.RunPython(add_sample_hotels, remove_sample_hotels),
    ]
