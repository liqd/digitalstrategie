function ValidateForm() {
    var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
    var formInput = document.getElementById('id_email')
    var inputValid = document.getElementById("id_email_valid")
    var inputInvalid = document.getElementById("id_email_invalid")
    var formCheckbox = document.getElementById('id_data_protection')
    var formCheckboxInvalid = document.getElementById("id_data_protection_invalid")
    var formCheckboxLabel = document.getElementById("id_data_protection_label")
    var formAction = document.getElementById("id_form_action")

    if(formInput.value.match(mailformat) && formCheckbox.checked)
      {
        formInput.classList.add("u-d-none")
        formCheckbox.classList.add("u-d-none")
        formCheckboxLabel.classList.add("u-d-none")
        inputValid.classList.remove("u-d-none")
        formCheckboxInvalid.classList.add("u-d-none")
        inputInvalid.classList.add("u-d-none")
        formAction.classList.add("u-d-none")
        document.getElementById("newsletter_form").submit()
        return false
      }
      else if (formInput.value.match(mailformat))
      {
        formCheckbox.classList.add("is-invalid")
        formCheckboxInvalid.classList.remove("u-d-none")
        formInput.classList.remove("is-invalid")
        inputInvalid.classList.add("u-d-none")
      }
      else if (formCheckbox.checked)
      {
        formInput.classList.add("is-invalid")
        inputInvalid.classList.remove("u-d-none")
        formCheckbox.classList.remove("is-invalid")
        formCheckboxInvalid.classList.add("u-d-none")
      }
      else
      {
        formInput.classList.add("is-invalid")
        formCheckbox.classList.add("is-invalid")
        formCheckboxInvalid.classList.remove("u-d-none")
        inputInvalid.classList.remove("u-d-none")
      document.newsletter_form.input2.focus()
      return false
      }
  }

function getCookie(name) {
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';')
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim()
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
              break
          }
      }
  }
  return cookieValue
}

var form = document.getElementById('newsletter_form'),
    input = document.createElement('input')

    input.name = "csrfmiddlewaretoken"
    input.type = "hidden"
    input.value = getCookie('csrftoken')

    form.appendChild(input)

window.ValidateForm = ValidateForm
