import math
from random import random
import json
import jsonschema
from jsonschema import validate

NUMBER_OF_PLAYERS = 2


all_cities_data = ['Абакан', 'Абердин', 'Абиджан', 'Абу-Даби', 'Абуджа', 'Абья-Палуоя', 'Авдеевка', 'Агра', 'Аддис-Абеба', 'Аделаида', 'Аден', 'Азов', 'Айдахо-Фолс', 'Айн-эль-Араб', 'Акерабат', 'Аккра', 'Аксай', 'Актау', 'Актобе', 'Алапаевск', 'Александрия', 'Алеппо', 'Алжир', 'Аликанте', 'Алитус', 'Алма-Ата', 'Алушта', 'Альбукерке', 'Альметьевск', 'Амман', 'Амритсар', 'Амстердам', 'Амстердам', 'Анадырь', 'Анапа', 'Анахайм', 'Ангарск', 'Ангрен', 'Анкара', 'Анталья', 'Антананариву', 'Антверпен', 'Антиохия', 'Антрацит', 'Аньер-сюр-Сен', 'Апатиты', 'Арамиль', 'Арзамас', 'Армавир', 'Армянск', 'Арсеньев', 'Артём', 'Архангельск', 'Асбест', 'Асино', 'Астрахань', 'Асуан', 'Асунсьон', 'Асьют', 'Атланта', 'Атырау', 'Аугсбург', 'Афины', 'Африн', 'Ахалкалаки', 'Ахалцих', 'Ахваз', 'Ахмадабад', 'Ахтубинск', 'Ачинск', 'Аш', 'Ашхабад', 'Баболь', 'Багдад', 'Баграм', 'Багратионовск', 'Базель', 'Баку', 'Балаклава', 'Балаково', 'Балашиха', 'Балтийск', 'Балтимор', 'Бамако', 'Бангалор', 'Бангкок', 'Бандар-Сери-Бегаван', 'Бандунг', 'Банжул', 'Барановичи', 'Барнаул', 'Барселона', 'Бартлсвилл', 'Басра', 'Бат', 'Батайск', 'Батон-Руж', 'Батуми', 'Бахчисарай', 'Беверли-Хиллз', 'Бейрут', 'Белая Калитва', 'Белая Церковь', 'Белгород', 'Белград', 'Белебей', 'Белёв', 'Белорецк', 'Белосток', 'Белу-Оризонти', 'Белфаст', 'Бельфор', 'Бендер-Аббас', 'Бендеры', 'Бербанк', 'Берген', 'Бердск', 'Бердянск', 'Березники', 'Берёзовский', 'Берестечко', 'Берлин', 'Беслан', 'Бехбехан', 'Бийск', 'Бир-Лелу', 'Бирмингем', 'Биробиджан', 'Бирск', 'Бишкек', 'Благовещенск', 'Блантайр', 'Бобровица', 'Бобруйск', 'Богородицк', 'Богородск', 'Богота', 'Бонн', 'Борисов', 'Боровичи', 'Бородино', 'Бостад', 'Бостон', 'Бохтар', 'Браззавиль', 'Бразилиа', 'Брайзах-на-Рейне', 'Брандон', 'Братислава', 'Братск', 'Браунау-ам-Инн', 'Брейнтри', 'Бремен', 'Брест', 'Брисбен', 'Брно', 'Брюссель', 'Брюссельский столичный регион', 'Брянск', 'Бугульма', 'Будапешт', 'Будённовск', 'Буинск', 'Буйнакск', 'Бука', 'Бурос', 'Буффало', 'Бухара', 'Бухарест', 'Бушир', 'Буэнос-Айрес', 'Бхубанешвар', 'Быдгощ', 'Вааса', 'Вагаршапат', 'Ваднагар', 'Вадуц', 'Валдай', 'Валенсия', 'Валлетта', 'Валмиера', 'Ванкувер', 'Вантаа', 'Варна', 'Варшава', 'Вашингтон', 'Веймар', 'Великие Луки', 'Великий Новгород', 'Веллингтон', 'Вельс', 'Вельск', 'Вена', 'Венерсборг', 'Венеция', 'Верхнеднепровск', 'Верхняя Пышма', 'Видное', 'Виктория', 'Виктория', 'Вильнюс', 'Вилюйск', 'Виндзор', 'Виндхук', 'Винница', 'Висагинас', 'Висбаден', 'Витебск', 'Вифлеем', 'Вичуга', 'Вишакхапатнам', 'Владивосток', 'Владикавказ', 'Владимир', 'Владимир-Волынский', 'Волгоград', 'Волгодонск', 'Волжский', 'Вологда', 'Волоколамск', 'Волочиск', 'Вольск', 'Вонсан', 'Воркута', 'Воронеж', 'Воскресенск', 'Воткинск', 'Вроцлав', 'Выборг', 'Выкса', 'Высоцк', 'Вышний Волочёк', 'Вьентьян', 'Вязьма', 'Гаага', 'Габала', 'Габороне', 'Гавана', 'Гагра', 'Газни', 'Галац', 'Галифакс', 'Галле', 'Гамбург', 'Гамильтон', 'Ганновер', 'Гао', 'Гаосюн', 'Гатчина', 'Гвадалахара', 'Гвадар', 'Гвалиор', 'Гватемала', 'Гданьск', 'Гдов', 'Гдыня', 'Гельзенкирхен', 'Генуя', 'Герасдорф-бай-Вин', 'Герат', 'Гермонасса', 'Герцлия', 'Гётеборг', 'Гилрой', 'Гирин', 'Гискар', 'Глазго', 'Глазов', 'Гливице', 'Глостер', 'Голд-Кост', 'Голицыно', 'Гомель', 'Гонолулу', 'Гори', 'Горно-Алтайск', 'Горохов', 'Гороховец', 'Грац', 'Грейт-Данмоу', 'Гренобль', 'Гродно', 'Грозный', 'Гронинген', 'Гуанчжоу', 'Гуково', 'Гусев', 'Гусь-Хрустальный', 'Гюмри', 'Гянджа', 'Давос', 'Дайр-эз-Заур', 'Дакар', 'Даллас', 'Далматово', 'Дальнереченск', 'Далянь', 'Дамаск', 'Дананг', 'Данидин', 'Дар-эс-Салам', 'Даръа', 'Дейтон', 'Дели', 'Делфт', 'Денвер', 'Дера-Исмаил-Хан', 'Дербент', 'Детройт', 'Джакарта', 'Джанкой', 'Джвари', 'Джексонвилл', 'Джелалабад', 'Джерабулус', 'Джибути', 'Джидда', 'Джохор-Бару', 'Дзержинск', 'Дзёэцу', 'Дмитров', 'Днепр', 'Долгопрудный', 'Домодедово', 'Донецк', 'Донецк', 'Дортмунд', 'Доха', 'Дрезден', 'Дрогобыч', 'Дружковка', 'Дуала', 'Дубай', 'Дублин', 'Дубна', 'Дубно', 'Дубоссары', 'Дувр', 'Дуйсбург', 'Дума', 'Думьят', 'Дунгуань', 'Дурбан', 'Душанбе', 'Дыре-Дауа', 'Дьёр', 'Дэбрэ-Зэйт', 'Дюртюли', 'Дюссельдорф', 'Евлах', 'Евле', 'Евпатория', 'Егорьевск', 'Екатеринбург', 'Елабуга', 'Елгава', 'Елец', 'Ельня', 'Енакиево', 'Енисейск', 'Ереван', 'Ессентуки', 'Жезказган', 'Железноводск', 'Железногорск', 'Женева', 'Жешув', 'Житомир', 'Жуковский', 'Заводоуковск', 'Загатала', 'Загреб', 'Запорожье', 'Звенигород', 'Зелёна-Гура', 'Зеленоград', 'Зеленоградск', 'Зеленодольск', 'Зёльден', 'Зефельд-ин-Тироль', 'Златоуст', 'Золотое', 'Зувара', 'Ивано-Франковск', 'Иваново', 'Ивантеевка', 'Ивдель', 'Игарка', 'Идлиб', 'Иерусалим', 'Ижевск', 'Измаил', 'Измир', 'Изюм', 'Илам', 'Индиан-Уэллс', 'Инсбрук', 'Инчхон', 'Иокогама', 'Ирбит', 'Иркутск', 'Исламабад', 'Исфахан', 'Ичня', 'Ишим', 'Ишимбай', 'Йезд', 'Йоханнесбург', 'Йошкар-Ола', 'Йоэнсуу', 'Йювяскюля', 'Кабо-Сан-Лукас', 'Кабул', 'Кавала', 'Кагарлык', 'Кадис', 'Казань', 'Каир', 'Калабасас', 'Каламазу', 'Калгари', 'Кали', 'Калининград', 'Калуга', 'Калуш', 'Калькутта', 'Камбарка', 'Каменец-Подольский', 'Каменка', 'Каменск-Уральский', 'Каменск-Шахтинский', 'Камень-Каширский', 'Камник', 'Кампала', 'Камышин', 'Камышлов', 'Кандагар', 'Канзас-Сити', 'Канны', 'Каннын', 'Каракас', 'Каратау', 'Карачи', 'Кардифф', 'Карловы Вары', 'Карлсруэ', 'Карпинск', 'Касабланка', 'Каспийск', 'Катав-Ивановск', 'Катайск', 'Катманду', 'Каунас', 'Кванджу', 'Кебили', 'Кейптаун', 'Келоуна', 'Кельме', 'Кёльн', 'Кембридж', 'Кемерово', 'Кеноша', 'Керман', 'Керманшах', 'Керчь', 'Кетчикан', 'Киверцы', 'Кигали', 'Киев', 'Кизляр', 'Кингисепп', 'Кингстон', 'Кингстон', 'Кинешма', 'Киншаса', 'Киото', 'Киркенес', 'Киркук', 'Киров', 'Кировград', 'Кирово-Чепецк', 'Кировск', 'Кирьят-Шмона', 'Кисловодск', 'Кисмайо', 'Китакюсю', 'Кито', 'Китченер', 'Кицбюэль', 'Кишинёв', 'Клагенфурт-ам-Вёртерзе', 'Клин', 'Кобе', 'Кобленц', 'Ковель', 'Ковров', 'Козьмодемьянск', 'Кола', 'Коломбо', 'Коломна', 'Коломыя', 'Колорадо-Спрингс', 'Коммунар', 'Комсомольск-на-Амуре', 'Конаково', 'Конакри', 'Кондопога', 'Конотоп', 'Константина', 'Константинополь', 'Копейск', 'Копенгаген', 'Кордова', 'Коркино', 'Королёв', 'Корсаков', 'Костанай', 'Костомукша', 'Кострома', 'Котка', 'Котону', 'Коувола', 'Кочабамба', 'Кошице', 'Крайстчерч', 'Краков', 'Краматорск', 'Кранстон', 'Красноармейск', 'Красногорск', 'Краснодар', 'Краснокамск', 'Красноперекопск', 'Краснотурьинск', 'Красноуфимск', 'Красноярск', 'Кременчуг', 'Криби', 'Кривой Рог', 'Кронштадт', 'Кропивницкий', 'Кропоткин', 'Кру', 'Кстово', 'Куала-Лумпур', 'Кубинка', 'Кузнецк', 'Кукмор', 'Кукута', 'Куляб', 'Кум', 'Кумамото', 'Кунгур', 'Куопио', 'Купертино', 'Курган', 'Куритиба', 'Курск', 'Кутаиси', 'Кучинг', 'Кызыл', 'Кыштым', 'Кэмпбелтаун', 'Кэрнс', 'Ла-Гуайра', 'Ла-Корунья', 'Ла-Пас', 'Лабытнанги', 'Лаваль', 'Лагос', 'Лаишево', 'Ланьчжоу', 'Лаппеэнранта', 'Лас-Вегас', 'Латакия', 'Лахор', 'Лахти', 'Лашкаргах', 'Лаэ', 'Ле-Ман', 'Леверкузен', 'Лезерхед', 'Лейпциг', 'Лександ', 'Леон-де-лос-Альдама', 'Лермонтов', 'Лесной', 'Лестер', 'Лиакватпур', 'Либревиль', 'Ливерпуль', 'Лидс', 'Лидчёпинг', 'Лима', 'Лимерик', 'Линц', 'Липецк', 'Лиссабон', 'Лобамба', 'Лобня', 'Лодзь', 'Лозанна', 'Лозовая', 'Ломе', 'Ломоносов', 'Лонгйир', 'Лондон', 'Лондон', 'Лос-Анджелес', 'Лохья', 'Луанда', 'Луга', 'Луганск', 'Луисвилл', 'Луксор', 'Лунд', 'Лусака', 'Луцк', 'Лыткарино', 'Львов', 'Льеж', 'Льейда', 'Люберцы', 'Люблин', 'Любляна', 'Любомль', 'Людиново', 'Люксембург', 'Люнебург', 'Магадан', 'Магас', 'Магнитогорск', 'Мадрид', 'Мазари-Шариф', 'Майами', 'Майданшахр', 'Майдугури', 'Майкоп', 'Майнц', 'Макао', 'Макеевка', 'Малая Вишера', 'Мале', 'Мальмё', 'Мамоново', 'Манагуа', 'Манама', 'Манаус', 'Манбидж', 'Мангейм', 'Манзини', 'Манила', 'Манчестер', 'Мапуту', 'Марави', 'Маракайбо', 'Мариб', 'Марракеш', 'Марсель', 'Мартуни', 'Марьинка', 'Маскат', 'Махачкала', 'Мбабане', 'Медвежьегорск', 'Медина', 'Междуреченск', 'Мезень', 'Мекка', 'Мелеуз', 'Мелитополь', 'Мельбурн', 'Меса', 'Мессина', 'Мехико', 'Мешхед', 'Мзузу', 'Миасс', 'Миккели', 'Милан', 'Минеральные Воды', 'Миннеаполис', 'Минск', 'Минусинск', 'Мирноград', 'Мирный', 'Мирный', 'Мичуринск', 'Могадишо', 'Могилёв', 'Модена', 'Можайск', 'Мозырь', 'Момбаса', 'Монктон', 'Монреаль', 'Монте-Карло', 'Монтевидео', 'Монтеррей', 'Монтрё', 'Москва', 'Мосул', 'Муданьцзян', 'Мукачево', 'Мумбаи', 'Мур', 'Мурманск', 'Муром', 'Мухосранск', 'Мытищи', 'Мюнхен', 'Набережные Челны', 'Нагано', 'Нагасаки', 'Нагоя', 'Назарет', 'Назрань', 'Найроби', 'Накхонратчасима', 'Нальчик', 'Нанкин', 'Нант', 'Наньпин', 'Наньтун', 'Наро-Фоминск', 'Нарьян-Мар', 'Нассау', 'Наха', 'Нахичевань', 'Находка', 'Нджамена', 'Неаполь', 'Невинномысск', 'Невьянск', 'Негомбо', 'Нерчинск', 'Нерюнгри', 'Несауалькойотль', 'Нефтекамск', 'Нефтеюганск', 'Ниамей', 'Нижневартовск', 'Нижнекамск', 'Нижние Серги', 'Нижний Новгород', 'Нижний Тагил', 'Никея', 'Николаев', 'Николаевск-на-Амуре', 'Никосия', 'Ниноцминда', 'Ницца', 'Нове-Место-на-Мораве', 'Нови-Сад', 'Нововолынск', 'Нововоронеж', 'Новокузнецк', 'Новокуйбышевск', 'Новомосковск', 'Новоржев', 'Новороссийск', 'Новосибирск', 'Новочебоксарск', 'Новочеркасск', 'Новошахтинск', 'Новый Орлеан', 'Новый Уренгой', 'Ногинск', 'Нойленгбах', 'Нойс', 'Норильск', 'Норман', 'Нортклифф', 'Ноттингем', 'Ноябрьск', 'Нуайон', 'Нуакшот', 'Нур-Султан', 'Нурвик', 'Нью-Дели', 'Нью-Йорк', 'Ньюпорт', 'Нэшвилл', 'Нюрнберг', 'Нючёпинг', 'Оберстдорф', 'Обихиро', 'Обнинск', 'Одесса', 'Одинцово', 'Озёры', 'Оита', 'Оклахома-Сити', 'Окленд', 'Окленд', 'Октябрьский', 'Олбани', 'Оленегорск', 'Ольгин', 'Омаха', 'Омск', 'Онича', 'Опа-лока', 'Оре', 'Орёл', 'Оренбург', 'Орехово-Зуево', 'Орландо', 'Орск', 'Оруро', 'Орхус', 'Орша', 'Осака', 'Осло', 'Острава', 'Оттава', 'Оулу', 'Охрид', 'Очаков', 'Ош', 'Павловский Посад', 'Павлодар', 'Паган', 'Палембанг', 'Палермо', 'Палм-Спрингс', 'Палу', 'Пальмира', 'Панама', 'Панама-Сити', 'Панкалпинанг', 'Паньцзинь', 'Парадайс', 'Париж', 'Паттайя', 'Певек', 'Пекин', 'Пенза', 'Первоуральск', 'Переславль-Залесский', 'Пермь', 'Перт', 'Петергоф', 'Петра', 'Петрозаводск', 'Петропавловск', 'Петропавловск-Камчатский', 'Пивденное', 'Пиза', 'Пикалёво', 'Пинск', 'Пионерский', 'Питерборо', 'Питтсбург', 'Плантейшен', 'Плейно', 'Плёс', 'Плоцк', 'Пномпень', 'Подгайцы', 'Подгорица', 'Подольск', 'Подпорожье', 'Познань', 'Полтава', 'Помпеи', 'Пори', 'Порт-Луи', 'Порт-о-Пренс', 'Порт-оф-Спейн', 'Портленд', 'Порто-Ново', 'Порту', 'Поти', 'Потоси', 'Почта Банк в Королёве', 'Почта Банк в Тюмени', 'Пошехонье', 'Прага', 'Претория', 'Принс-Альберт', 'Приозерск', 'Припять', 'Провиденс', 'Прокопьевск', 'Псков', 'Пудун', 'Пули-Хумри', 'Пуна', 'Пусан', 'Пушкин', 'Пушкино', 'Пуэбла-де-Сарагоса', 'Пхукет', 'Пятигорск', 'Рабат', 'Равалпинди', 'Рамалла', 'Рамат-Ган', 'Раменское', 'Ранн', 'Рединг', 'Рединг', 'Рейкьявик', 'Реутов', 'Решт', 'Ржев', 'Рига', 'Риека', 'Ризе', 'Рим', 'Рио-де-Жанейро', 'Ричмонд', 'Рованиеми', 'Ровно', 'Рожище', 'Ромны', 'Россошь', 'Ростов', 'Ростов-на-Дону', 'Роттердам', 'Рочестер', 'Рошаль', 'Рубцовск', 'Рузаевка', 'Рыбинск', 'Рыбник', 'Ряжск', 'Рязань', 'Сазерленд-Спрингс', 'Сайтама', 'Сакраменто', 'Салават', 'Салехард', 'Сало', 'Салоники', 'Самара', 'Самарканд', 'Самаро', 'Самарра', 'Сан-Антонио', 'Сан-Антонио-дель-Тачира', 'Сан-Бруно', 'Сан-Диего', 'Сан-Паулу', 'Сан-Сальвадор', 'Сан-Фелиу-де-Гишольс', 'Сан-Франциско', 'Сан-Хосе', 'Сан-Хосе', 'Сан-Хуан', 'Сан-Хуан', 'Сана', 'Санкт-Петербург', 'Санта-Клара', 'Санта-Клара', 'Санта-Кларита', 'Санта-Крус-де-ла-Сьерра', 'Санта-Моника', 'Санта-Фе', 'Санта-Элена-де-Уайрен', 'Санто-Доминго', 'Сантьяго', 'Сапопан', 'Саппоро', 'Сарагоса', 'Сараево', 'Саранск', 'Сарапул', 'Саратов', 'Сари-Пуль', 'Саров', 'Саскатун', 'Саут-Бенд', 'Сафоново', 'Свебодзин', 'Светлогорск', 'Светлодарск', 'Светлый', 'Севастополь', 'Северный Огден', 'Северодвинск', 'Североморск', 'Североуральск', 'Северск', 'Севилья', 'Сегежа', 'Сеговия', 'Сейняйоки', 'Секешфехервар', 'Сёльвесборг', 'Семикаракорск', 'Сендай', 'Сент-Луис', 'Сергиев Посад', 'Серов', 'Серпухов', 'Сестрорецк', 'Сеул', 'Сехван-Шариф', 'Сиань', 'Сибай', 'Сиди-Беннур', 'Сидней', 'Силькеборг', 'Симферополь', 'Сингапур', 'Сирджан', 'Сиэтл', 'Скопье', 'Славянск', 'Славянск-на-Кубани', 'Смоленск', 'Снежинск', 'Снежное', 'Советск', 'Советск', 'Солигорск', 'Солнечногорск', 'Солсбери', 'Солт-Лейк-Сити', 'Солфорд', 'Сортавала', 'София', 'Сочи', 'Спасск-Дальний', 'Спирмен', 'Среднеуральск', 'Сретенск', 'Ставрополь', 'Стамбул', 'Старый Оскол', 'Степанакерт', 'Стерлинг', 'Стерлитамак', 'Стокгольм', 'Страсбург', 'Струмица', 'Судак', 'Сукре', 'Сумы', 'Сунжа', 'Сурабая', 'Сургут', 'Сусуман', 'Сухой Лог', 'Сухум', 'Сучжоу', 'Суэц', 'Счастье', 'Сызрань', 'Сыктывкар', 'Сьюдад-Хуарес', 'Сямынь', 'Таганрог', 'Таиз', 'Тайбэй', 'Тайчжун', 'Тайынша', 'Таллин', 'Таманрассет', 'Тамбов', 'Тампа', 'Тампере', 'Таншань', 'Тарапото', 'Таррагона', 'Тарту', 'Таузанд-Окс', 'Ташкент', 'Таштагол', 'Тбилиси', 'Тверь', 'Тебриз', 'Тегеран', 'Тегусигальпа', 'Тель-Авив', 'Темников', 'Темрюк', 'Терни', 'Тернополь', 'Тёфу', 'Тилбург', 'Тимбукту', 'Тирана', 'Тирасполь', 'Тихуана', 'Тобольск', 'Токио', 'Тольятти', 'Томск', 'Торецк', 'Торонто', 'Тосно', 'Трабзон', 'Тренчьянске-Теплице', 'Трёхгорный', 'Триполи', 'Трир', 'Трнава', 'Трускавец', 'Тршинец', 'Туапсе', 'Тувумба', 'Тула', 'Тулуза', 'Тулун', 'Тунис', 'Турин', 'Турку', 'Тэгу', 'Тэджон', 'Тюмень', 'Тяньцзинь', 'Уагадугу', 'Углич', 'Ужгород', 'Уилмингтон', 'Украинка', 'Улан-Батор', 'Улан-Удэ', 'Ульяновск', 'Умаг', 'Умео', 'Умм-эль-Баваки', 'Уолтем', 'Уорик', 'Уотертаун', 'Уотфорд', 'Уральск', 'Урумчи', 'Урюпинск', 'Усинск', 'Уссурийск', 'Устилуг', 'Усть-Каменогорск', 'Усть-Катав', 'Усть-Лабинск', 'Уфа', 'Ухань', 'Ухта', 'Уэст-Палм-Бич', 'Фарах', 'Фарнборо', 'Феодосия', 'Фиери', 'Филадельфия', 'Финикс', 'Флоренция', 'Форт-Лодердейл', 'Форт-Уэрт', 'Фошань', 'Франкфурт-на-Майне', 'Фрязино', 'Фукуока', 'Фучжоу', 'Фушунь', 'Хабаровск', 'Хайдарабад', 'Хайфа', 'Хакодате', 'Хала', 'Хама', 'Хан-Шейхун', 'Ханой', 'Ханты-Мансийск', 'Ханчжоу', 'Хараре', 'Харбин', 'Харлем', 'Хартум', 'Харьков', 'Хасавюрт', 'Хашури', 'Хельсингборг', 'Хельсинки', 'Херенвен', 'Херсон', 'Херсонес Таврический', 'Химки', 'Хиросима', 'Хихон', 'Хмельницкий', 'Хобарт', 'Ход-ха-Шарон', 'Ходейда', 'Ходжалы', 'Хониара', 'Хоторн', 'Хохфильцен', 'Хошимин', 'Хуанган', 'Хуахин', 'Худжанд', 'Хулун-Буир', 'Хуэйчжоу', 'Хьюстон', 'Хэфэй', 'Хямеэнлинна', 'Целе', 'Цзинань', 'Цзинин', 'Цзиньхуа', 'Цзянмэнь', 'Циндао', 'Цинциннати', 'Цуг', 'Цхинвали', 'Цюаньчжоу', 'Цюрих', 'Чанша', 'Чарлстон', 'Часов Яр', 'Чебаркуль', 'Чебоксары', 'Чеджу', 'Челябинск', 'Ченнаи', 'Череповец', 'Черкассы', 'Черкесск', 'Чернигов', 'Чернобыль', 'Черновцы', 'Черногорск', 'Черняховск', 'Чжанцзяган', 'Чжаоцин', 'Чжэнчжоу', 'Чиангмай', 'Чикаго', 'Чико', 'Чита', 'Чкаловск', 'Чолпон-Ата', 'Чугуев', 'Чунцин', 'Чусовой', 'Чьерна-над-Тисоу', 'Чэнду', 'Шадринск', 'Шали', 'Шаморин', 'Шанхай', 'Шарлотт', 'Шарм-эш-Шейх', 'Шатура', 'Шахты', 'Шахунья', 'Шацк', 'Шемахы', 'Шеффилд', 'Шибарган', 'Шилале', 'Шилка', 'Шинданд', 'Шираз', 'Шиханы', 'Шиханы 2', 'Штутгарт', 'Шуша', 'Шымкент', 'Шэньчжэнь', 'Шэньян', 'Щавница', 'Щёлково', 'Щецин', 'Ыгдыр', 'Эверетт', 'Эдинбург', 'Эдмонтон', 'Эймсбери', 'Эйндховен', 'Эклсхолл', 'Электренай', 'Электрогорск', 'Электросталь', 'Элиста', 'Эль-Ариш', 'Эль-Аюн', 'Эль-Гиза', 'Эль-Камышлы', 'Эль-Кувейт', 'Эль-Пасо', 'Эль-Сегундо', 'Эль-Хилла', 'Эльблонг', 'Эн-Наджаф', 'Энгельс', 'Энергодар', 'Эр-Ракка', 'Эр-Рияд', 'Эрак', 'Эрбиль', 'Эрншёльдсвик', 'Эрфурт', 'Эспоо', 'Эссен', 'Эстерсунд', 'Эфес', 'Эшборн', 'Южная Тарава', 'Южно-Сахалинск', 'Юма', 'Юрмала', 'Юрюзань', 'Яань', 'Ябинг', 'Якутск', 'Ялта', 'Ялуторовск', 'Ямусукро', 'Янгон', 'Яньтай', 'Яньчэн', 'Яремче', 'Ярославль', 'Яунде']


schema = {
    "type": "object",
    "properties": {
        "players": {
            "type": "array",
            "minItems": NUMBER_OF_PLAYERS,
            "maxItems": NUMBER_OF_PLAYERS,
            "items": {
                "username": {"type": "string"}
            }
        },
        "cities": {
            "type": "array",
            "items": {
                "city": {"type": "string"}
            }
        }
    },
    "required": [
        "players",
        "cities"
    ]
}


def create_player(username, cities, client):
    return Player(username, cities, client)


def parse_data(data):
    players = list()
    cities = list()
    for cities_data in data['cities']:
        cities.append(cities_data['city'])
    for player_data in data['players']:
        player = Player(player_data['username'],
                        cities,
                        None)
        players.append(player)
    return players


def init_players():
    players = list()
    cities = ['Самара']
    for i in range(0, NUMBER_OF_PLAYERS):
        players.append(
            create_player(
                f"player{i}", cities, None
            )
        )
    return players


def validate_json(data):
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def load_game_state_from_json(json_file_path):
    with open(json_file_path) as json_file:
        try:
            data = json.load(json_file)
            if validate_json(data):
                return True, data
        except json.decoder.JSONDecodeError:
            pass
    return False, None


def dump_game_state_to_json(players, cities, json_file_path):
    data = {'players': [], "cities": []}
    for player in players:
        data['players'].append(player.dict())
    for city in cities:
        data['cities'].append({'city': city})
    with open(json_file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def delete_probel(city):
    i = -1
    while city[i] == ' ':
        i -= 1
        print(i, city[i])
    if i == -1:
        return city
    return city[:i+1]

class Player:

    def __init__(self, username, cities, client_socket):
        self.username = username
        self.cities = cities
        self.client_socket = client_socket

    def __str__(self):
        return f"Player username: {self.username}"

    def move(self, city):
        city = delete_probel(city)
        self.cities.append(city)

    def can_move(self, city):
        city = delete_probel(city)
        condition0 = len(city)!=0
        if condition0:
            if self.cities[-1][-1] in 'ъыь':
                condition1 = (self.cities[-1][-2] == (city.lower())[0])
            else:
                condition1 = (self.cities[-1][-1] == (city.lower())[0])
        else:
            condition1 = False
        condition2 = city in all_cities_data
        return (condition0 and condition1 and condition2) or city == 'Give up'

    def fail(self, city):
        return (city in set(self.cities)) or (city == 'Give up')

    def dict(self):
        return {
            'username': self.username
        }
