const API_KEY = '5e690a505730fa2354d7f86895a89102';
const BASE_URL = 'https://api.themoviedb.org/3';
const IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500';

// Get query from URL
const urlParams = new URLSearchParams(window.location.search);
const query = urlParams.get('query');

// Get container to display results
const resultsContainer = document.getElementById('searchResults');

async function searchMovies(query) {
    try {
        const response = await fetch(`${BASE_URL}/search/movie?api_key=${API_KEY}&query=${encodeURIComponent(query)}`);
        if (!response.ok) throw new Error('Failed to fetch search results');
        const data = await response.json();
        return data.results;
    } catch (error) {
        console.error('Error searching movies:', error);
        return [];
    }
}

function displayMovies(movies, container) {
    container.innerHTML = '';
    if (movies.length === 0) {
        container.innerHTML = '<p>No movies found.</p>';
        return;
    }
    movies.forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.className = 'movie-card';
        movieCard.innerHTML = `
            <a href="movie.html?id=${movie.id}">
                <img src="${movie.poster_path ? IMAGE_BASE_URL + movie.poster_path : 'https://via.placeholder.com/500x750?text=No+Poster'}"
                alt="${movie.title}" class="movie-poster">
            </a>
            <div class="movie-info">
                <a href="movie.html?id=${movie.id}">
                    <h3 class="movie-title">${movie.title}</h3>
                </a>
                <p class="movie-year">${movie.release_date ? movie.release_date.split('-')[0] : 'N/A'}</p>
                <div class="movie-rate">
                    <i class="fas fa-star"></i>
                    <span>${movie.vote_average.toFixed(1)}</span>
                </div>
            </div>
        `;
        container.appendChild(movieCard);
    });
}

// Only run if query exists
if (query) {
    searchMovies(query).then(movies => displayMovies(movies, resultsContainer));
}