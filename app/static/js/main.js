// ===== DROPDOWN TOGGLE (DESKTOP) =====
function toggleMenu(event, menuId, fallbackUrl) {
  event.preventDefault();
  const menu = document.getElementById(menuId);

  // Close all other dropdowns
  document.querySelectorAll('.dropdown-menu').forEach(function(m) {
    if (m.id !== menuId) m.classList.remove('show');
  });

  // Toggle this dropdown
  if (menu) {
    menu.classList.toggle('show');
  }

  // If already showing and clicked again, navigate
  if (menu && !menu.classList.contains('show') && fallbackUrl) {
    window.location.href = fallbackUrl;
  }
}

// ===== CLOSE DROPDOWNS ON OUTSIDE CLICK =====
document.addEventListener('click', function(e) {
  const isDropdownLink = e.target.closest('.desktop-menu > li');
  if (!isDropdownLink) {
    document.querySelectorAll('.dropdown-menu').forEach(function(m) {
      m.classList.remove('show');
    });
  }
});

// ===== MOBILE MENU TOGGLE =====
function toggleMobileMenu() {
  const menu = document.getElementById('mobile-menu');
  if (menu) {
    menu.classList.toggle('show');
  }
}

// ===== MOBILE SUBMENU TOGGLE =====
function toggleMobileSubmenu(submenuId) {
  const submenu = document.getElementById(submenuId);
  if (submenu) {
    submenu.classList.toggle('show');
  }
}

// ===== AOS INITIALIZATION =====
document.addEventListener('DOMContentLoaded', function() {
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 800,
      easing: 'ease-out',
      once: true,
      offset: 80
    });
  }
});

// ===== FAQ ACCORDION =====
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.faq-question').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const item = this.closest('.faq-item');
      // Close all others
      document.querySelectorAll('.faq-item').forEach(function(faq) {
        if (faq !== item) faq.classList.remove('open');
      });
      item.classList.toggle('open');
    });
  });
});

// ===== VACANCY MODALS =====
document.addEventListener('DOMContentLoaded', function() {
  // Open modal via data-modal attribute
  document.querySelectorAll('[data-modal]').forEach(function(trigger) {
    trigger.addEventListener('click', function() {
      const modalId = this.getAttribute('data-modal');
      const overlay = document.getElementById(modalId);
      if (overlay) {
        openModal(overlay);
      }
    });
  });

  // Close modal via data-modal-close attribute
  document.querySelectorAll('[data-modal-close]').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const overlay = this.closest('.modal-overlay');
      if (overlay) closeModal(overlay);
    });
  });

  // Close modal when clicking on the overlay background
  document.querySelectorAll('.modal-overlay').forEach(function(overlay) {
    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) {
        closeModal(overlay);
      }
    });
  });

  // Close modal on ESC key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay.open').forEach(function(overlay) {
        closeModal(overlay);
      });
    }
  });
});

function openModal(overlay) {
  overlay.classList.add('open');
  document.body.classList.add('modal-open');
  // Focus the close button for accessibility
  const closeBtn = overlay.querySelector('.modal-close');
  if (closeBtn) closeBtn.focus();
}

function closeModal(overlay) {
  overlay.classList.remove('open');
  // Only remove body lock if no other modals are open
  const anyOpen = document.querySelector('.modal-overlay.open');
  if (!anyOpen) {
    document.body.classList.remove('modal-open');
  }
}
