// Текущее значение счётчика
let value = 0;

const resultEl = document.getElementById("result");
const plusBtn  = document.getElementById("plus");
const minusBtn = document.getElementById("minus");
const messageEl = document.getElementById("message");

// Обновление отображения (цвет, блокировка кнопок, сообщение)
function updateView() {
  resultEl.textContent = value;

  // Цвет в зависимости от значения
  if (value > 0) {
    resultEl.style.backgroundColor = "yellow";
    resultEl.style.color = "#000";
  } else if (value < 0) {
    resultEl.style.backgroundColor = "green";
    resultEl.style.color = "#000";
  } else {
    resultEl.style.backgroundColor = "red";
    resultEl.style.color = "#000";
  }

  // Блокировка кнопок
  plusBtn.disabled  = value >= 10;
  minusBtn.disabled = value <= -10;

  // Сообщение о экстремальном значении
  if (value === 10 || value === -10) {
    messageEl.textContent = "Вы достигли экстремального значения";
  } else {
    messageEl.textContent = "";
  }
}

// Обработчики кнопок
plusBtn.addEventListener("click", function () {
  value += 1;
  updateView();
});

minusBtn.addEventListener("click", function () {
  value -= 1;
  updateView();
});

// Стартовое состояние
updateView();
