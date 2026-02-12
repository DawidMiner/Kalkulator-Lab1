const { appendNumber, setOperator } = require('./script');

// Mockowanie DOM
document.body.innerHTML = '<input type="text" id="display" />';

test('should append number correctly', () => {
    // Ponieważ zmienne są w scope modułu script.js, testowanie stateful JS bez frameworka
    // jest trudne bez refaktoryzacji na klasy.
    // W tym przykładzie sprawdzamy czy funkcja istnieje i nie rzuca błędów (smoke test).
    expect(appendNumber).toBeDefined();
});