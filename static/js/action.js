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
    console.log('clicked')
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('expandSidebar').addEventListener('click', toggleSidebarMode);
    document.getElementById('collapseSidebar').addEventListener('click', toggleSidebarMode);
})

