function toggleSidebarMode() {
    const sidebar = document.getElementById('sidebar');
    const compactSidebar = document.getElementById('compactSidebar');
    const fullSidebarContent = document.getElementById('fullSidebarContent');
    // const mainContent = document.getElementById('mainContent');
    
    const isCompact = !fullSidebarContent.classList.contains('hidden');
    
    if (isCompact) {
        // Switch to compact sidebar
        compactSidebar.classList.remove('hidden');
        compactSidebar.classList.add('lg:flex');
        fullSidebarContent.classList.add('hidden');
        sidebar.classList.remove('w-64');
        sidebar.classList.add('w-16');
        // mainContent.classList.remove('lg:ml-64');
        // mainContent.classList.add('lg:ml-16');
    } else {
        // Switch to full sidebar
        compactSidebar.classList.remove('lg:flex');
        compactSidebar.classList.add('hidden');
        fullSidebarContent.classList.remove('hidden');
        sidebar.classList.remove('w-16');
        sidebar.classList.add('w-64');
        // mainContent.classList.remove('lg:ml-16');
        // mainContent.classList.add('lg:ml-64');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('expandSidebar').addEventListener('click', toggleSidebarMode);
    document.getElementById('collapseSidebar').addEventListener('click', toggleSidebarMode);
})

