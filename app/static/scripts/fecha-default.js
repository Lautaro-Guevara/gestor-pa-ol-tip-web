



export function fechaDefaultForm(query) {
  const today = new Date().toISOString().split('T')[0];
  const fechaInput = document.querySelector(query)

  fechaInput.value = today
}