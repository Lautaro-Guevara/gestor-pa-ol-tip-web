const fechaInput = document.getElementById('fecha');

  // Establecer la fecha actual por defecto
  const today = new Date().toISOString().split('T')[0];
  fechaInput.value = today;