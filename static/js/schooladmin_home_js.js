// Get the modal elements
const modal = document.getElementById("postModal");
const startPostButton = document.getElementById("startPostButton");
const closeModalBtn = document.querySelector(".close");
const submitModalPostBtn = document.getElementById("submitModalPost");

// Array to store posts
let posts = [];
let notifications = [];

// Open the modal when clicking on "Start a post" input
startPostButton.addEventListener("click", function() {
    modal.style.display = "block";
});

// Close the modal when clicking on the close button
closeModalBtn.addEventListener("click", function() {
    modal.style.display = "none";
});

// Close the modal when clicking outside of the modal content
window.addEventListener("click", function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});

// Handle submitting the post from the modal
submitModalPostBtn.addEventListener("click", function() {
    const modalPostContent = document.getElementById('modalPostContent').value;

    if (modalPostContent) {
        const post = {
            content: modalPostContent,
            likes: 0,
            id: posts.length
        };
        posts.push(post);
        renderPosts();
        modal.style.display = "none"; // Close the modal
        document.getElementById('modalPostContent').value = ''; // Clear the textarea
    }
});

// Render the posts to the feed
function renderPosts() {
    const feed = document.getElementById('feed');
    feed.innerHTML = '';
    posts.forEach((post, index) => {
        feed.innerHTML += `
            <div class="feed-post">
                <p>${post.content}</p>
                <button onclick="likePost(${index})">Like (${post.likes})</button>
                <button onclick="commentPost(${index})">Comment</button>
            </div>
        `;
    });
}

// Like post function
function likePost(postId) {
    posts[postId].likes += 1;
    addNotification(`Someone liked your post: "${posts[postId].content}"`);
    renderPosts();
}

// Add a notification
function addNotification(message) {
    notifications.push(message);
    renderNotifications();
}

// Render the notifications
function renderNotifications() {
    const notificationList = document.getElementById('notificationList');
    notificationList.innerHTML = '';
    notifications.forEach((notification) => {
        notificationList.innerHTML += `<li>${notification}</li>`;
    });
}

/* Custom Dropdown JavaScript */

// Get elements
const dropdownSelected = document.querySelector('.dropdown-selected');
const dropdownOptions = document.querySelector('.dropdown-options');
const dropdownItems = document.querySelectorAll('.dropdown-options li');

// Toggle dropdown options on click
dropdownSelected.addEventListener('click', function () {
    dropdownOptions.style.display = dropdownOptions.style.display === 'block' ? 'none' : 'block';
});

// Handle selecting an option
dropdownItems.forEach(function (item) {
    item.addEventListener('click', function () {
        // Update selected option
        const iconSrc = item.querySelector('img').src;
        const text = item.textContent.trim();
        dropdownSelected.innerHTML = `<img src="${iconSrc}" alt="Selected Icon" class="option-icon" /><span>${text}</span>`;

        // Hide options
        dropdownOptions.style.display = 'none';
    });
});

// Hide dropdown if clicked outside
document.addEventListener('click', function (event) {
    if (!event.target.closest('.custom-dropdown')) {
        dropdownOptions.style.display = 'none';
    }
});
