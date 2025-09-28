function toggleSidebarMode() {
    const sidebar = document.getElementById('sidebar');
    const compactSidebar = document.getElementById('compactSidebar');
    const items = compactSidebar.querySelectorAll('.btn-title')
    // const mainContent = document.getElementById('mainContent');

    const isCompact = !sidebar.classList.contains('w-64');
    console.log(isCompact)

    if (isCompact) {
        // Switch to compact sidebar
        items.forEach(item => {
            item.className = 'btn-title absolute font-medium ml-8'
        })
        sidebar.classList.remove('w-16');
        sidebar.classList.add('w-64');
        

    } else {
        // Switch to full sidebar
        items.forEach(item => {
            item.className = 'btn-title absolute left-full ml-2 px-2 py-1 bg-gray-800 text-white text-xs rounded opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap'  
        })
        sidebar.classList.remove('w-64');
        sidebar.classList.add('w-16');
        
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('expandSidebar').addEventListener('click', toggleSidebarMode);
    document.getElementById('collapseSidebar').addEventListener('click', toggleSidebarMode);
})

