function checkAge(age) { //Using a question mark operator '?'
    return (age > 18) ? true : confirm('Did parents allow you?');
}

function checkAge(age) {//Using OR || (the shortest variant)
    return (age > 18) || confirm('Did parents allow you?');
}