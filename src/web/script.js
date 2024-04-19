let expression = '';



function appendToDisplay(value) {
    expression += value;
    document.getElementById('display').value = expression;
}

function clearDisplay() {
    expression = '';
    document.getElementById('display').value = '';
    document.getElementById('output').value = '';
}

async function calculate() {

    try {
        let result = await eel.calculate(expression)();
        document.getElementById('output').value = result
        expression = result.toString();
    } catch (error) {
        console.log(error)
        document.getElementById('output').value = 'Error';
    }
}
