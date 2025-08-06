// filepath: d:\Day 8\movieApp\js\movie.js
const API_KEY = '5e690a505730fa2354d7f86895a89102';
const BASE_URL = 'https://api.themoviedb.org/3';
const IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500';

const urlParams = new URLSearchParams(window.location.search);
const movieId = urlParams.get('id');
const movieDetailsContainer = document.getElementById('movieDetails');

async function fetchMovieDetails(id) {
    try {
        const response = await fetch(`${BASE_URL}/movie/${id}?api_key=${API_KEY}`);
        if (!response.ok) throw new Error('Failed to fetch movie details');
        return await response.json();
    } catch (error) {
        console.error('Error fetching movie details:', error);
        return null;
    }
}

function displayMovieDetails(movie) {
    if (!movie) {
        movieDetailsContainer.innerHTML = '<p>Movie details not found.</p>';
        return;
    }
    movieDetailsContainer.innerHTML = `
        <div class="movie-detail-card">
            <img src="${movie.poster_path ? IMAGE_BASE_URL + movie.poster_path : 'https://via.placeholder.com/500x750?text=No+Poster'}"
                alt="${movie.title}" class="movie-poster-large">
            <div class="movie-detail-info">
                <h2>${movie.title}</h2>
                <p><strong>Release Date:</strong> ${movie.release_date || 'N/A'}</p>
                <p><strong>Rating:</strong> <i class="fas fa-star"></i> ${movie.vote_average.toFixed(1)}</p>
                <p><strong>Overview:</strong> ${movie.overview || 'No overview available.'}</p>
                <p><strong>Genres:</strong> ${movie.genres.map(g => g.name).join(', ') || 'N/A'}</p>
                <p><strong>Runtime:</strong> ${movie.runtime ? movie.runtime + ' min' : 'N/A'}</p>
            </div>
        </div>
    `;
}

if (movieId) {
    fetchMovieDetails(movieId).then(displayMovieDetails);
}