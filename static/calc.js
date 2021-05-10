function adder(x, y) {
    return x + y;
}

$('#calc-form').on('submit', (evt) =>{
    evt.preventDefault();

    const x = parseInt($('#x-field').val());
    const y = parseInt($('#y-field').val());

    $('#result').text(adder(x, y));
});