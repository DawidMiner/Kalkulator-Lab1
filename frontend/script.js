let currentInput = "";
let previousInput = "";
let operator = null;

function appendNumber(number) {
    currentInput += number;
    updateDisplay();
}

function updateDisplay() {
    document.getElementById('display').value = currentInput;
}

function setOperator(op) {
    if (currentInput === "") return;
    operator = op;
    previousInput = currentInput;
    currentInput = "";
}

function clearDisplay() {
    currentInput = "";
    previousInput = "";
    operator = null;
    updateDisplay();
}

async function calculate() {
    if (operator === null || currentInput === "") return;

    const payload = {
        num1: parseFloat(previousInput),
        num2: parseFloat(currentInput),
        operator: operator
    };

    try {
        const response = await fetch('/api/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const err = await response.json();
            alert("Błąd: " + err.detail);
            clearDisplay();
            return;
        }

        const data = await response.json();
        currentInput = data.result.toString();
        operator = null;
        previousInput = "";
        updateDisplay();
    } catch (e) {
        alert("Błąd połączenia z serwerem");
    }
}

// Eksport dla testów (Node.js environment check)
if (typeof module !== 'undefined') {
    module.exports = { appendNumber, setOperator };
}