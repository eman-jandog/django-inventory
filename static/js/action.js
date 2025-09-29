function toggleSidebarMode() {
    const sidebar = document.getElementById('sidebar');
    const fullSidebar = document.getElementById('fullSidebar');
    // const mainContent = document.getElementById('mainContent');

    const isCompact = !sidebar.classList.contains('w-64');

    if (isCompact) {
        // Switch to compact sidebar
        sidebar.classList.remove('w-16');
        sidebar.classList.add('w-64');
        

    } else {
        // Switch to full sidebar
        sidebar.classList.remove('w-64');
        sidebar.classList.add('w-16');
        
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

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('expandSidebar').addEventListener('click', toggleSidebarMode);
    document.getElementById('btnProfile').addEventListener('click', toggleUserMenu);

    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', () => {
            const section = item.dataset.section;
            showSection(section);
        })
    })

    document.addEventListener('click', function(event) {
        const userMenu = document.getElementById('userMenu');
        
        if (!userMenu.classList.contains('hidden')) {
            const userButton = event.target.closest('button');  
            
            if (!userButton || userButton.getAttribute('id') != 'btnProfile') {
                userMenu.classList.add('hidden');
            }
        }
    });

    showSection('overview')
})


