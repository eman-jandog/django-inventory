// Technical Functions

function handleLogout() {
    // localStorage.removeItem('userEmail');
    // localStorage.removeItem('isLoggedIn');
    
    // Show auth container and hide dashboard
    document.getElementById('dashboardContainer').classList.add('hidden');
    // document.getElementById('authContainer').classList.remove('hidden');
    
    // Reset forms
    document.getElementById('loginFormElement').reset();
    document.getElementById('registerFormElement').reset();
    showLoginForm();
}

function toggleSidebarMode() {
    const sidebar = document.getElementById('sidebar'); 
    const mainContent = document.getElementById('mainContent');

    const isCompact = !sidebar.classList.contains('w-64');

    if (isCompact) {
        // Switch to compact sidebar
        sidebar.classList.remove('w-16');
        sidebar.classList.add('w-64');
        mainContent.classList.remove('lg:ml-16');
        mainContent.classList.add('lg:ml-64');      
    } else {
        // Switch to full sidebar
        sidebar.classList.remove('w-64');
        sidebar.classList.add('w-16');
        mainContent.classList.remove('lg:ml-64');
        mainContent.classList.add('lg:ml-16');  
    }
}

function showSection(sectionName) {
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('bg-blue-50', 'text-blue-600', 'border-r-2', 'border-blue-600');
        item.classList.add('text-gray-600', 'hover:bg-gray-50', 'hover:text-gray-800');

        if (item.dataset.section == sectionName) {
            item.classList.remove('text-gray-600', 'hover:bg-gray-50', 'hover:text-gray-800');
            item.classList.add('bg-blue-50', 'text-blue-600', 'border-r-2', 'border-blue-600');
        }
    })   
}

function toggleUserMenu() {
    const sidebar = document.getElementById('sidebar'); 
    const userMenu = document.getElementById('userMenu');

    const isCompact = sidebar.classList.contains('w-16');

    if (isCompact) {
        userMenu.classList.remove('lg:left-66');
        userMenu.classList.add('lg:left-18')
    }
    else {
        userMenu.classList.remove('lg:left-18')
        userMenu.classList.add('lg:left-66');
    }

    userMenu.classList.toggle('hidden');
}

// Initializing

function initializeCharts() {
    // Asset Distribution Chart
    const assetCtx = document.getElementById('assetChart').getContext('2d');
    new Chart(assetCtx, {
        type: 'doughnut',
        data: {
            labels: ['Laptops', 'Monitors', 'Mobile Devices', 'Printers', 'Accessories'],
            datasets: [{
                data: [35, 25, 20, 12, 8],
                backgroundColor: [
                    '#3B82F6',
                    '#10B981',
                    '#F59E0B',
                    '#EF4444',
                    '#8B5CF6'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        usePointStyle: true
                    }
                }
            }
        }
    });

    // Monthly Orders Chart
    const ordersCtx = document.getElementById('ordersChart').getContext('2d');
    new Chart(ordersCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [{
                label: 'Orders',
                data: [12, 19, 15, 25, 22, 30],
                borderColor: '#3B82F6',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

function initializeDashboard() {
    // populateStaffTable();
    // populateOrdersTable();
    // populateAssetsGrid();
    // loadUserProfile();
    
    // Initialize charts after a short delay to ensure DOM is ready
    setTimeout(initializeCharts, 100);
}

document.addEventListener('DOMContentLoaded', () => {
    // Single Listeners
    document.getElementById('logoutBtn').addEventListener('click', handleLogout);
    document.getElementById('profileBtn').addEventListener('click', toggleUserMenu);
    document.getElementById('sidebarToggle').addEventListener('click', toggleSidebarMode);

    // Multiple Listeners
    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', () => {
            const section = item.dataset.section;
            showSection(section);
        })
    })

    // Situational Listeners
    document.addEventListener('click', function(event) {
        const userMenu = document.getElementById('userMenu');
        
        if (!userMenu.classList.contains('hidden')) {
            const userButton = event.target.closest('button');  
            
            if (!userButton || userButton.getAttribute('id') != 'profileBtn') {
                userMenu.classList.add('hidden');
            }
        }
    });

    //  Initial Run
    showSection('overview');
    toggleSidebarMode();
    initializeDashboard();
})


