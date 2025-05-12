/* script.js */
const pokedex = document.getElementById('pokedex');

async function fetchPokemon(id) {
  const url = `https://pokeapi.co/api/v2/pokemon/${id}`;
  const response = await fetch(url);
  const data = await response.json();

  const speciesResponse = await fetch(data.species.url);
  const speciesData = await speciesResponse.json();

  const frenchNameEntry = speciesData.names.find(entry => entry.language.name === 'fr');
  const name = frenchNameEntry ? frenchNameEntry.name : data.name;

  return {
    id: data.id,
    name: name,
    img: data.sprites.front_default,
    cry: `https://play.pokemonshowdown.com/audio/cries/${data.name.toLowerCase()}.mp3`
  };
}

async function loadPokedex() {
  for (let i = 1; i <= 151; i++) {
    const pokemon = await fetchPokemon(i);
    const col = document.createElement('div');
    col.className = 'col';
    col.innerHTML = `
      <div class="card h-100">
        <img src="${pokemon.img}" class="card-img-top animate__animated animate__pulse" alt="${pokemon.name}" style="cursor: pointer;">
        <div class="card-body">
          <h5 class="card-title">${pokemon.name}</h5>
          <p class="card-text">#${pokemon.id.toString().padStart(3, '0')}</p>
        </div>
      </div>
    `;

    const img = col.querySelector('img');
    img.addEventListener('click', () => {
      const audio = new Audio(pokemon.cry);
      audio.play();
      img.classList.remove('animate__pulse');
      void img.offsetWidth; // reset animation
      img.classList.add('animate__pulse');
    });

    pokedex.appendChild(col);
  }
}

// Ajouter Animate.css
const link = document.createElement('link');
link.rel = 'stylesheet';
link.href = 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css';
document.head.appendChild(link);

loadPokedex();

