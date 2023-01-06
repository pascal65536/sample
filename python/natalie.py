number = 1982
sum_digit = 0
while number > 0:
    sum_digit = sum_digit + number % 10
    number = number // 10
print(sum_digit)


natal_dct = {
    '1': 'Для вас характерны выдающиеся творческие способности, свобода суждений и способность мыслить весьма новаторски. Вы — активны, предприимчивы и очень энергичны. Цифра один символизирует чувство ответственности и напористости, поэтому такие, как вы, закономерно (хотя и по желанию) оказываются в кресле директора. Единица — идеальная оценка для успешной карьеры. В любви люди с числом судьбы 1 — верные и надежные партнеры, в большинстве случаев играющие доминирующую роль в отношениях.',
    '2': 'Неспроста двойка символизирует противоречие противоположностей — обладателям этого числа жизненного пути регулярно приходится бороться с перепадами настроения и даже депрессией, но в то же время вы добры и сердечны. Несмотря на разносторонние таланты, семейные ценности и забота о близких всегда будут для вас в приоритете. Вы умеете смекалисто и быстро разрешать конфликты, а в работе — справляться с любыми трудностями. Поскольку вам свойственно залипать на чужих интересах, почаще вспоминайте, что заботиться надо и о себе.',
    '3': 'Те, кому выпала тройка, раскрываются в жизни как харизматичные оптимисты, которым рады окружающие. Вы популярны среди друзей, успешны в работе и покоряете любые цели благодаря креативному подходу и самодисциплине. Тем не менее, успех нередко привлекает внимание завистников, что не только расстраивает вас, но и создает преграды для движения вперед. Для обладателей числа судьбы 3 очень важно встретить настоящую любовь, хотя порой вам нелегко понять чувства других и проявить эмпатию.',
    '4': 'Четверка воплощает собой целостность — недаром квадрат имеет четыре угла, а знаки зодиака делятся на четыре стихии. Люди с этим числом жизненного пути обладают проницательным умом, впечатляющим даром организатора и неизменно полагаются на логику. Из-за пунктуальности, методичности и прямой манеры высказываться вас часто воспринимают как персонажа с жестким характером, но внутренняя гармония и спокойный нрав обеспечивают вам верных друзей и стабильные отношения.',
    '5': 'Вы — выдающийся оратор, умеете расположить к себе любого собеседника или мотивировать команду. Вам присущи гибкость в общении, открытость, доброжелательность. Обладатели числа жизненного пути 5 любят свободу и обожают приключения, стараясь по возможности игнорировать повседневную рутину и долгосрочные обязательства. Очевидные для вас приоритеты усложняют отношения с родственниками, партнерами и коллегами, но на такого харизматика, как вы, просто невозможно долго обижаться.',
    '6': 'Шестерка символизирует устойчивость и истину. Если вам выпало это число жизненного пути, вы — перфекционист, вдохновляемый гармонией и красотой, творческая, мечтательная личность с обостренным чувством справедливости и большими амбициями. Вам хватает такта угадать ситуацию, где требуется ваша помощь, ни в коем случае не вмешиваясь в чужие дела без повода. Скорее всего, вы раскроетесь в творческой профессии, а в отношениях — как однолюб/-ка, потому что партнер просто обязан соответствовать вашим высоким стандартам.',
    '7': 'Семерка — магическое, мощное число, определяющее человека уравновешенного, уверенного, представительного, обладающего талантом распознавать человеческие натуры. Ваша интуиция настроена на самые тонкие вибрации, и у вас есть духовная жилка, наделяющая способностью нести знания людям. Стоит обратить внимание на важный нюанс: вас тяготит верность, пока вы не встретите любовь своей жизни, поэтому будьте начеку, если не хотите ее упустить.',
    '8': 'Если вам выпала восьмерка, вы штурмом покорите карьерную лестницу. Такие, как вы, ориентированы на успех, мыслят практично, искренне хотят заработать много денег и обладают тягой к соперничеству. Вы обладаете активной жизненной позицией и всегда готовы взять инициативу в свои руки. Сила воли ведет вас к любой из ваших целей, хотя и быстро слабнет под гнетом чужой критики. При этом на отношения ваша уверенность не распространяется — в любви вы недоверчивы и ревнивы.',
    '9': 'Под номером девять проходит жизненный путь позитивной, деятельной и скромной личности, которую нелегко разгадать. С одной стороны, с виду вы социально активны, умеете быть душой компании и готовы на все ради близких. С другой стороны, вы позволяете себе откровенничать лишь с избранными, пряча от остальных свои эмоции. Тем не менее, в любви вы полностью оттаиваете, отменяя все границы и барьеры ради сердечной привязанности.',
}

day_of_birdth = input('Введите дату рождения в формате ддммггг: ')  # '08101974'
while len(day_of_birdth) > 1:
    sum_digit = 0
    for d in day_of_birdth:
        sum_digit += int(d)
    day_of_birdth = str(sum_digit)
print('Значиение числа судьбы', day_of_birdth)
print(natal_dct[day_of_birdth])

