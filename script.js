const API_URL = 'http://127.0.0.1:8000';
const bookListElement = document.getElementById('book-list');
const loadingMessage = document.getElementById('loading-message');
const addBookForm = document.getElementById('add-book-form');
const isbnInput = document.getElementById('isbn-input');
const searchInput = document.getElementById('search-input');
const modal = document.getElementById('book-detail-modal');
const modalTitle = document.getElementById('modal-title');
const modalAuthor = document.getElementById('modal-author');
const modalISBN = document.getElementById('modal-isbn');
const modalImage = document.getElementById('modal-image');
const closeModalButton = document.getElementById('close-modal');

let allBooks = [];

async function fetchBooks() {
    try {
        loadingMessage.style.display = 'block';
        const response = await fetch(`${API_URL}/books`);
        if (!response.ok) {
            throw new Error(`HTTP hatası! Durum: ${response.status}`);
        }
        allBooks = await response.json();
        renderBooks(allBooks);
    } catch (error) {
        bookListElement.innerHTML = `<p class="col-span-full text-red-400 text-center">Kitaplar yüklenirken bir hata oluştu: ${error.message}</p>`;
    } finally {
        loadingMessage.style.display = 'none';
    }
}

function renderBooks(booksToRender) {
    bookListElement.innerHTML = '';
    if (booksToRender.length === 0) {
        bookListElement.innerHTML = '<p class="col-span-full text-center text-gray-400">Kütüphanede henüz kitap yok.</p>';
    } else {
        booksToRender.forEach(book => {
            const bookItem = document.createElement('div');
            bookItem.className = "p-4 card cursor-pointer relative group flex gap-4 items-center";
            bookItem.innerHTML = `
                <img src="${book.image_url || 'https://placehold.co/80x120/4b386a/FFFFFF?text=Yok'}" alt="${book.title} kapağı" class="book-cover">
                <div class="flex-grow">
                    <h3 class="text-lg font-medium">${book.title}</h3>
                    <p class="text-sm text-gray-300">Yazar: ${book.author}</p>
                    <p class="text-xs text-gray-400">ISBN: ${book.ISBN}</p>
                </div>
                <button onclick="event.stopPropagation(); deleteBook('${book.ISBN}')" class="absolute top-2 right-2 bg-red-600 text-white p-1 rounded-full text-xs opacity-0 group-hover:opacity-100 transition-opacity shadow-sm">&times;</button>
            `;
            bookItem.addEventListener('click', () => showBookDetails(book));
            bookListElement.appendChild(bookItem);
        });
    }
}

async function addBook(event) {
    event.preventDefault();
    const isbn = isbnInput.value.trim();
    if (!isbn) {
        alert('Lütfen bir ISBN numarası girin.');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/add-by-isbn/${isbn}`, {
            method: 'POST'
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(`API hatası: ${error.detail}`);
        }
        
        alert('Kitap başarıyla eklendi!');
        isbnInput.value = '';
        fetchBooks();
    } catch (error) {
        alert(`Kitap eklenirken bir hata oluştu: ${error.message}`);
    }
}

async function deleteBook(isbn) {
    if (!confirm('Bu kitabı silmek istediğinize emin misiniz?')) {
        return;
    }
    try {
        const response = await fetch(`${API_URL}/books/${isbn}`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            throw new Error(`HTTP hatası! Durum: ${response.status}`);
        }

        alert('Kitap başarıyla silindi!');
        fetchBooks();
    } catch (error) {
        alert(`Kitap silinirken bir hata oluştu: ${error.message}`);
    }
}

function searchBooks() {
    const query = searchInput.value.toLowerCase();
    const filteredBooks = allBooks.filter(book => 
        book.title.toLowerCase().includes(query) || 
        book.author.toLowerCase().includes(query) || 
        book.ISBN.toLowerCase().includes(query)
    );
    renderBooks(filteredBooks);
}

function showBookDetails(book) {
    modalTitle.textContent = book.title;
    modalAuthor.textContent = book.author;
    modalISBN.textContent = book.ISBN;
    modalImage.src = book.image_url || 'https://placehold.co/150x225/4b386a/FFFFFF?text=Yok';
    modal.classList.add('modal-open', 'opacity-100', 'pointer-events-auto');
}

function hideBookDetails() {
    modal.classList.remove('modal-open', 'opacity-100', 'pointer-events-auto');
}

window.onload = fetchBooks;
addBookForm.addEventListener('submit', addBook);
searchInput.addEventListener('input', searchBooks);
closeModalButton.addEventListener('click', hideBookDetails);

