// LegalGapDB Website JavaScript

// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80; // Account for fixed nav
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Update active nav item based on scroll position
    updateActiveNav();
    window.addEventListener('scroll', updateActiveNav);

    // Load dynamic statistics
    loadStatistics();

    // Mobile menu toggle
    setupMobileMenu();
});

function updateActiveNav() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('nav a[href^="#"]');
    
    let current = '';
    const scrollY = window.pageYOffset;
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        const sectionHeight = section.offsetHeight;
        
        if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('text-legal-blue', 'font-semibold');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('text-legal-blue', 'font-semibold');
        }
    });
}

function loadStatistics() {
    // In a real implementation, this would fetch from an API
    // For now, we'll use static data that matches our seed cases
    
    const stats = {
        totalCases: 20,
        countries: 1,
        domains: 5,
        averageGap: 35.2, // Average compliance gap across all cases
        lastUpdated: new Date().toISOString().split('T')[0]
    };
    
    // Update DOM elements
    const statCases = document.getElementById('stat-cases');
    if (statCases) {
        animateNumber(statCases, 0, stats.totalCases, 1500);
    }
    
    // Add country breakdown if element exists
    const countryStats = document.getElementById('country-stats');
    if (countryStats) {
        countryStats.innerHTML = generateCountryStatsHTML();
    }
    
    // Add domain breakdown if element exists
    const domainStats = document.getElementById('domain-stats');
    if (domainStats) {
        domainStats.innerHTML = generateDomainStatsHTML();
    }
}

function animateNumber(element, start, end, duration) {
    const startTime = performance.now();
    
    function updateNumber(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        const current = Math.floor(start + (end - start) * progress);
        element.textContent = current;
        
        if (progress < 1) {
            requestAnimationFrame(updateNumber);
        }
    }
    
    requestAnimationFrame(updateNumber);
}

function generateCountryStatsHTML() {
    const countries = [
        { code: 'AR', name: 'Argentina', cases: 20, flag: '🇦🇷' },
        { code: 'BR', name: 'Brazil', cases: 0, flag: '🇧🇷', coming: 'Q2 2026' },
        { code: 'MX', name: 'Mexico', cases: 0, flag: '🇲🇽', coming: 'Q3 2026' },
        { code: 'IN', name: 'India', cases: 0, flag: '🇮🇳', coming: 'Q3 2026' },
        { code: 'NG', name: 'Nigeria', cases: 0, flag: '🇳🇬', coming: 'Q4 2026' }
    ];
    
    return countries.map(country => {
        const comingText = country.coming ? ` • Coming ${country.coming}` : '';
        return `
            <div class="flex items-center justify-between p-4 bg-white rounded-lg shadow">
                <div class="flex items-center space-x-3">
                    <span class="text-2xl">${country.flag}</span>
                    <div>
                        <div class="font-semibold">${country.name}</div>
                        <div class="text-sm text-gray-600">${country.code}${comingText}</div>
                    </div>
                </div>
                <div class="text-right">
                    <div class="text-2xl font-bold text-legal-blue">${country.cases}</div>
                    <div class="text-sm text-gray-600">cases</div>
                </div>
            </div>
        `;
    }).join('');
}

function generateDomainStatsHTML() {
    const domains = [
        { name: 'Labor Law', cases: 5, icon: '👨‍💼' },
        { name: 'Tax Law', cases: 4, icon: '💰' },
        { name: 'Corporate Law', cases: 4, icon: '🏢' },
        { name: 'Criminal Law', cases: 4, icon: '⚖️' },
        { name: 'Family Law', cases: 2, icon: '👨‍👩‍👧‍👦' },
        { name: 'Administrative Law', cases: 1, icon: '🏛️' }
    ];
    
    const totalCases = domains.reduce((sum, domain) => sum + domain.cases, 0);
    
    return domains.map(domain => {
        const percentage = Math.round((domain.cases / totalCases) * 100);
        return `
            <div class="flex items-center justify-between p-4 bg-white rounded-lg shadow">
                <div class="flex items-center space-x-3">
                    <span class="text-2xl">${domain.icon}</span>
                    <div>
                        <div class="font-semibold">${domain.name}</div>
                        <div class="text-sm text-gray-600">${percentage}% of cases</div>
                    </div>
                </div>
                <div class="text-right">
                    <div class="text-2xl font-bold text-legal-blue">${domain.cases}</div>
                    <div class="text-sm text-gray-600">cases</div>
                </div>
            </div>
        `;
    }).join('');
}

function setupMobileMenu() {
    // Add mobile menu button to navigation
    const nav = document.querySelector('nav .flex');
    const mobileButton = document.createElement('button');
    mobileButton.className = 'md:hidden text-gray-700 hover:text-legal-blue p-2';
    mobileButton.innerHTML = `
        <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
    `;
    
    // Add mobile menu
    const mobileMenu = document.createElement('div');
    mobileMenu.className = 'md:hidden hidden bg-white border-t border-gray-200';
    mobileMenu.innerHTML = `
        <div class="px-4 py-2 space-y-2">
            <a href="#home" class="block px-3 py-2 text-gray-700 hover:text-legal-blue">Home</a>
            <a href="#about" class="block px-3 py-2 text-gray-700 hover:text-legal-blue">About</a>
            <a href="#cases" class="block px-3 py-2 text-gray-700 hover:text-legal-blue">Cases</a>
            <a href="#contribute" class="block px-3 py-2 text-gray-700 hover:text-legal-blue">Contribute</a>
            <a href="browse.html" class="block px-3 py-2 text-gray-700 hover:text-legal-blue">Browse</a>
        </div>
    `;
    
    // Toggle mobile menu
    mobileButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
    
    // Add to DOM
    nav.appendChild(mobileButton);
    nav.parentElement.appendChild(mobileMenu);
}

// Case search and filtering for browse page
function initializeBrowse() {
    if (!document.getElementById('case-search')) return;
    
    const searchInput = document.getElementById('case-search');
    const countryFilter = document.getElementById('country-filter');
    const domainFilter = document.getElementById('domain-filter');
    const caseGrid = document.getElementById('case-grid');
    
    // Load and display cases
    loadAndDisplayCases();
    
    // Set up event listeners
    searchInput?.addEventListener('input', filterCases);
    countryFilter?.addEventListener('change', filterCases);
    domainFilter?.addEventListener('change', filterCases);
}

function loadAndDisplayCases() {
    // In a real implementation, this would fetch from an API
    // For now, we'll use static data representing our seed cases
    
    const cases = [
        {
            id: 'AR-LAB-001',
            title: 'Informal Labor: Registration and Social Security Gap',
            country: 'Argentina',
            domain: 'Labor Law',
            gapValue: 40.1,
            gapUnit: 'percent',
            description: 'Law requires worker registration within 5 days. Reality: 40.1% of workers operate without formal registration.',
            tags: ['informality', 'social_security', 'enforcement_gap']
        },
        {
            id: 'AR-TAX-001',
            title: 'VAT Evasion: Legal Obligation vs. Actual Collection',
            country: 'Argentina',
            domain: 'Tax Law',
            gapValue: 32.0,
            gapUnit: 'percent',
            description: 'Law requires 21% VAT on sales. Reality: 32% VAT gap due to systematic evasion.',
            tags: ['tax_evasion', 'vat', 'compliance']
        },
        {
            id: 'AR-CRIM-001',
            title: 'Economic Crimes Conviction Rate',
            country: 'Argentina',
            domain: 'Criminal Law',
            gapValue: 23.1,
            gapUnit: 'percent',
            description: 'Law criminalizes economic crimes. Reality: Only 23.1% conviction rate for initiated cases.',
            tags: ['economic_crimes', 'conviction_rate', 'judicial_system']
        }
        // Add more cases as needed
    ];
    
    displayCases(cases);
}

function displayCases(cases) {
    const caseGrid = document.getElementById('case-grid');
    if (!caseGrid) return;
    
    caseGrid.innerHTML = cases.map(case_ => `
        <div class="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
            <div class="flex items-center justify-between mb-4">
                <div>
                    <h3 class="font-bold text-lg text-legal-dark">${case_.title}</h3>
                    <p class="text-sm text-gray-600">${case_.id} • ${case_.country}</p>
                </div>
                <span class="px-3 py-1 bg-blue-100 text-blue-800 text-sm rounded-full">${case_.domain}</span>
            </div>
            
            <p class="text-gray-700 mb-4">${case_.description}</p>
            
            <div class="bg-red-50 p-3 rounded-lg mb-4">
                <div class="text-sm font-semibold text-red-800">Gap Size</div>
                <div class="text-2xl font-bold text-red-600">${case_.gapValue}${case_.gapUnit === 'percent' ? '%' : ''}</div>
            </div>
            
            <div class="flex flex-wrap gap-2 mb-4">
                ${case_.tags.map(tag => `<span class="px-2 py-1 bg-gray-100 text-gray-700 text-xs rounded">${tag}</span>`).join('')}
            </div>
            
            <a href="#${case_.id}" class="text-legal-blue font-semibold hover:underline">
                View Full Case →
            </a>
        </div>
    `).join('');
}

function filterCases() {
    // Implementation for filtering cases based on search and filters
    // This would be connected to the actual case data
    console.log('Filtering cases...');
}

// Initialize appropriate functionality based on page
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('case-search')) {
            initializeBrowse();
        }
    });
} else {
    if (document.getElementById('case-search')) {
        initializeBrowse();
    }
}

// Utility functions
function formatNumber(num) {
    return num.toLocaleString();
}

function formatPercentage(num) {
    return `${num.toFixed(1)}%`;
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}