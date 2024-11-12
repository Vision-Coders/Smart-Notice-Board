function addNewDiv() {
    const container = document.getElementById('dynamic-divs-container');

    const newDiv = document.createElement('div');
    newDiv.classList.add('new-div');

    // Close button
    const closeButton = document.createElement('button');
    closeButton.innerHTML = '✖';
    closeButton.classList.add('close-button');
    closeButton.onclick = () => container.removeChild(newDiv);

    // Name field
    const nameField = document.createElement('input');
    nameField.type = 'text';
    nameField.placeholder = 'Name';
    nameField.classList.add('input-field');

    // ID field
    const idField = document.createElement('input');
    idField.type = 'text';
    idField.placeholder = 'ID';
    idField.classList.add('input-field');

    // Text area
    const textArea = document.createElement('textarea');
    textArea.placeholder = 'Enter text here...';
    textArea.classList.add('textarea-field');

    // Submit button
    const submitButton = document.createElement('button');
    submitButton.innerHTML = 'Submit';
    submitButton.classList.add('submit-button');
    submitButton.onclick = () => alert('Submitted!');

    newDiv.appendChild(closeButton);
    newDiv.appendChild(nameField);
    newDiv.appendChild(idField);
    newDiv.appendChild(textArea);
    newDiv.appendChild(submitButton);

    container.appendChild(newDiv);
  }
