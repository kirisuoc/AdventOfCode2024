const fs = require('fs');

// Leemos el archivo input.txt
fs.readFile('input.txt', 'utf8', (err, text) => {
  if (err) {
    console.error(err);
    return;
  }

  // Expresión regular para las reglas (pares de números separados por '|')
  const ruleRegex = /\d+\|\d+/g;
  let rules = text.match(ruleRegex);

  // Expresión regular para las actualizaciones (números separados por comas)
  const updateRegex = /^(?:\d{1,3},)*\d{1,3}(?=\n|$)/gm;
  let updates = text.match(updateRegex);

  // Función para validar una actualización
  function validateUpdate(rules, pages) {
    for (const rule of rules) {
      const [x, y] = rule.split('|').map(Number);

      if (pages.includes(x) && pages.includes(y)) {
        if (pages.indexOf(x) > pages.indexOf(y)) {
          return false; // Si la página x aparece después de y, es inválida
        }
      }
    }
    return true; // Si todas las reglas se cumplen, la actualización es válida
  }

  // Función para corregir una actualización
  function fixUpdate(rules, pages) {
    let isValid = false;

    while (!isValid) {
      isValid = true;

      for (const rule of rules) {
        const [x, y] = rule.split('|').map(Number);

        if (pages.includes(x) && pages.includes(y)) {
          const indexX = pages.indexOf(x);
          const indexY = pages.indexOf(y);

          // Si x aparece después de y, intercambiamos las posiciones
          if (indexX > indexY) {
            [pages[indexX], pages[indexY]] = [pages[indexY], pages[indexX]];
            isValid = false; // La actualización aún no es válida, así que seguimos corrigiendo
          }
        }
      }
    }

    return pages; // Devolvemos la lista corregida
  }

  // Función para sumar los valores intermedios de las actualizaciones
  function sumMiddleValues(rules, updates) {
    let sum = 0;

    for (const update of updates) {
      // Aseguramos que 'update' es una cadena antes de hacer split
      const pages = update.split(',').map(Number);

      // Si la actualización no es válida, la corregimos
      if (!validateUpdate(rules, pages)) {
        const corrected = fixUpdate(rules, pages);
        const middleIndex = Math.floor(corrected.length / 2);
        sum += corrected[middleIndex]; // Sumamos el valor en el medio
      }
    }

    return sum;
  }

  // Llamamos a la función y mostramos el resultado
  console.log(sumMiddleValues(rules, updates));
});
