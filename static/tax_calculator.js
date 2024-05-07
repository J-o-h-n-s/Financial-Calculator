// This function strips non-numeric characters from the input.
function formatInput(input) {
    return input.replace(/[^\d.]/g, '');
}

// This function updates the salary fields and makes an AJAX request to the Flask backend.
function calculateAndUpdateSalaries() {
    const inputId = $(this).attr('id');
    const inputValue = parseFloat(formatInput($(this).val())); // Clean input before parsing
    const taxBracket = $('#tax_bracket').val();

    const salaryType = (inputId === 'yearly_salary') ? 'yearly' : 'monthly';

    $.post('/calculate', {
        salary_type: salaryType,
        salary: inputValue,
        tax_bracket: taxBracket
    }, function(data) {
        $('#yearly_salary').val(data.yearly_salary);
        $('#monthly_salary').val(data.monthly_salary);
        $('#net_monthly_salary').text('Net Monthly Salary: ' + data.net_monthly_salary);
    }).fail(function() {
        console.log("Error in calculation");
    });
}

$(document).ready(function() {
    // Bind the event handlers upon document ready
    $('#yearly_salary, #monthly_salary').change(calculateAndUpdateSalaries);
    $('#tax_bracket').change(calculateAndUpdateSalaries);

    // Event handler for formatting the input field on each key stroke
    $('#yearly_salary, #monthly_salary').on('input', function() {
        $(this).val(formatInput($(this).val()));
    });
});
