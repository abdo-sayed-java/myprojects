const API_KEY = '5e690a505730fa2354d7f86895a89102';
const BASE_URL = 'https://api.themoviedb.org/3';
const IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500';

//Assigning the BASE variables:
const nowPlayingGrid = document.getElementById("nowPlaying");
const popularMovieGrid = document.getElementById("popularMovies");
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById('searchBtn');

//FETCH MOVIES
async function fetchMovies(endpoint) {
    try {
        const response = await fetch(`${BASE_URL}${endpoint}?api_key=${API_KEY}`);
        if (!response.ok){ throw new Error ('Failed to Fetch Movies') }
        const data = await response.json();
        return data.results;
    } catch (error) {
        console.error('Error Fetching movies:', error);
        return [];
    }
}

function displayMovies(movies, container) {
    container.innerHTML = '';

    movies.forEach(movie => {
       const movieCard  = document.createElement('div');
        movieCard.className = 'movie-card'
        movieCard.innerHTML = `
        <a href="movie.html?id=${movie.id}">
            <img src="${movie.poster_path ? IMAGE_BASE_URL + movie.poster_path : 'https://via.placeholder.com/500x750?text=No+Poster'}"
            alt = "${movie.title}"
            class="movie-poster">
        </a>
        <div class="movie-info">
            <a href="movie.html?id=${movie.id}">
                <h3 class="movie-title">${movie.title}</h3>
            </a>
            <p class="movie-year">${movie.release_date ? movie.release_date.split('-')[0]: 'N/A'}</p>
            <div class="movie-rate">
                <i class="fas fa-star"></i>
                <span>${movie.vote_average.toFixed(1)}</span>
            </div>
        </div>
    `;
    container.appendChild(movieCard); 
    });
}

searchBtn.addEventListener('click', () => {
    const query = searchInput.value.trim();
    if (query) {
        window.location.href = `search.html?query=${encodeURIComponent(query)}`;
    }
})

searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const query = searchInput.value.trim();
        if (query) {
            window.location.href = `search.html?query=${encodeURIComponent(query)}`;
        }
    }
})

async function init() {
    const [nowPlaying, popular] = await Promise.all([
        fetchMovies('/movie/now_playing'),
        fetchMovies('/movie/popular')
    ]);

    displayMovies(nowPlaying, nowPlayingGrid);
    displayMovies(popular, popularMovieGrid);
}

init();