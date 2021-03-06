'use strict';
function start_program() {

    var selection = parseInt(prompt("Введите:\n1 для выбора конверетра валют;\n2 для игры в загадки;\n3 для вычисления уравнения\n4 банковская программа (рассчёт прибыли по вкладу)."));
    if (selection == 1) {
        conv_curr();
    }
    else if (selection == 2) {
        arcana();
    }
    else if (selection == 3) {
        equation();
    }
    else if (selection == 4) {
        bank_prog();
    }
    else {
        alert("Ответ не распознан.");
    }
}

function conv_curr() {
    var eur = 69.29; // Курс Евро
    var doll = 63.22; // Курс Доллара
    var rub = +(prompt("Введите сумму в рублях (только число):"));
    if (rub >= 0) {
        alert("Ваша сумма " + rub + " рубля(ей) после пересчёта составляет:\n " + (rub / doll).toFixed(2) + " долларов (по курсу " + doll + ")\n " + (rub / eur).toFixed(2) + " евро (по курсу " + eur + ")");
    }
    else {
        alert("Нужно было ввести число (только число - количество рублей)");
    }
}

function arcana_template(question, answer) {
    var user_answer = prompt(question);
    if ( user_answer.toLowerCase() == answer.toLowerCase() ) {
        alert("Поздравляю! Вы угадали. Теперь перейдем к следующей загадке.");
        return 1;
    }
    else {
        alert("Вы не угадали. Теперь перейдем к следующей загадке.");
        return 0;
    }
}

function arcana() {
    var count = 0;
    count += arcana_template("Первая загадка:\n С какой птицы нужно ощипать перья, чтобы получились сразу и утро, и день, и вечер, и ночь?", "с утки");

    count += arcana_template("Вторая загадка:\n Под каким деревом сидит волк, когда идет дождь?", "под мокрым");

    count += arcana_template("Третья загадка:\n На теле – два уха, а головы нет.", "кастрюля");

    count += arcana_template("Четвёртая (последняя) загадка:\n Что достанет зубами затылок?", "расчёска");

    alert("Было задано 4 загадки. Общее количесвто правильных ответов: " + count);
}

function equation() {
    var a = 2;
    var b = -1;
    var c = 4;
    var x = prompt("Вычисляем значение уравнения y=a*x^2+b*x+c, где a=" + a + ", b=" + b + ", c=" + c + ". Введите значение переменной x:");
    alert('При x="' + x + '" формула "y=(' + a + ')*x^2+(' + b + ')*x+(' + c + ')", равна ' + ((a*x*x) + b*x + c) );
}

function bank_prog() {
    var deposit = +prompt("Введите сумму вклада:");
    var percent = +prompt("Введите годовой процент по вкладу:");
    var time = 5;
    var sum = [];
    sum[0] = deposit;
    var result = 'Размер вклада на ближайшие 5 лет:';
    for (var i = 1; i <= time; i++) {
        sum[i] = (sum[i-1] * (100 + percent) / 100).toFixed(2);
        result += '\n' + i + ' год: ' + sum[i]
    }
    alert(result);
}
