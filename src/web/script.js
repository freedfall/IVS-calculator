let expression = '';



function appendToDisplay(value) {
    expression += value;
    document.getElementById('display').value = expression;
}

function clearDisplay() {
    expression = '';
    document.getElementById('display').value = '';
}

async function calculate() {

    try {
        let result = await eel.calculate(expression)();
        document.getElementById('display').value = result
        expression = result.toString();
    } catch (error) {
        console.log(error)
        document.getElementById('display').value = 'Error';
    }
}
