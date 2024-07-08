const userNameField = document.querySelector("[name=Nombre]");
const userApellidoField = document.querySelector("[name=Apellido]");
const telefonoField = document.querySelector("[name=Teléfono");
const emailField = document.querySelector("[name=email]");
const consultaField = document.querySelector("[name=Consulta]");
const correoField = document.querySelector("[name=Correo2]");
const fileField = document.querySelector("[name=file");

const validateEmptyField = (e) => {
    const field = e.target;
    const fieldValue = e.target.value;
    console.log(field);
    console.log(fieldValue);
    console.log(e.target.parentElement);
    console.log(field.nextElementSibling);
    if (fieldValue.trim().length === 0) {
       /*field.parentElement.insertAdjacentHTML(
        "beforeend",
        '<span class="error">Aviso error</span>'
       ) */
       field.classList.add("invalid");
       
       field.nextElementSibling.classList.add("error");
       field.nextElementSibling.innerText = `${field.name} es requerido`;
    } else {
        field.classList.remove("invalid");
        field.nextElementSibling.classList.remove("error");
        field.nextElementSibling.innerText = "";
    }
}

const validateEmailFormat = e => {
    const field = e.target;
    const fieldValue = e.target.value;
    const regex = new RegExp(/^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/);
    if (fieldValue.trim().length > 5 && !regex.test(fieldValue)) {
       /*field.parentElement.insertAdjacentHTML(
        "beforeend",
        '<span class="error">Aviso error</span>'
       ) */
       field.classList.add("invalid");
       field.nextElementSibling.classList.add("error");
       field.nextElementSibling.innerText = "Por favor ingresa un email válido";
    } else {
        field.classList.remove("invalid");
        field.nextElementSibling.classList.remove("error");
        field.nextElementSibling.innerText = "";
    }   
} 

userNameField.addEventListener("blur", validateEmptyField);
userApellidoField.addEventListener("blur", validateEmptyField);
telefonoField.addEventListener("blur", validateEmptyField);
emailField.addEventListener("blur", validateEmptyField);
consultaField.addEventListener("blur", validateEmptyField);
correoField.addEventListener("blur", validateEmptyField);

emailField.addEventListener("input", validateEmailFormat);
correoField.addEventListener("input", validateEmailFormat);


fileField.addEventListener("change", (e) => {
    const field = e.target;
    const fileExt = e.target.files[0].name.split(".").pop().toLowerCase();
    const allowedExt = ["jpg", "jpeg", "png", "gif"];
    if (!allowedExt.includes(fileExt)) {
        field.classList.add("invalid");
       field.nextElementSibling.classList.add("error");
       field.nextElementSibling.innerText = "Por favor ingresa un archivo con extensión jpg, jpeg, png o gif";

    } else {
        field.classList.remove("invalid");
        field.nextElementSibling.classList.remove("error");
        field.nextElementSibling.innerText = "";
    }

})
function validarFormulario() {
    // Obtener todos los campos de entrada del formulario
    const inputs = document.querySelectorAll(".table-responsive > input");
    console.log(inputs);
    
    // Recorrer todos los campos de entrada
    for (var i = 0; i < inputs.length; i++) {
        // Si el campo está vacío
        if (inputs[i].value.trim() === "") {
            // Mostrar un mensaje de error
            var fieldName = document.querySelector("label[for='" + inputs[i].id + "']").innerText;
            alert("Por favor, completa el campo: " + fieldName);
            // Prevenir el envío del formulario
            return false;
        }
    }
    // Si todos los campos están completos, permitir el envío del formulario
    return true;
}

    /**const field = e.target;
    const fieldValue = e.target.value;
    if (fieldValue.length === 0) {**/
       /*field.parentElement.insertAdjacentHTML(
        "beforeend",
        '<span class="error">Aviso error</span>'
       ) */
      /**  field.classList.add("invalid");
       field.nextElementSibling.classList.add("error");
       field.nextElementSibling.innerText = "El nombre es requerido";
    } else {
        field.classList.remove("invalid");
        field.nextElementSibling.classList.remove("error");
        field.nextElementSibling.innerText = "";
    }
}) */
