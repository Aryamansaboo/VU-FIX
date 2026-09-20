/**
 * VUFIX — Hostel Maintenance & Complaint Management System
 * Main Application Logic & View Controller (app.js)
 * Vanilla ES6+ Javascript
 */

document.addEventListener('DOMContentLoaded', () => {
  const store = window.VUFIXStore;

  // Active state filters
  let currentStudentFilter = 'all';
  let currentStudentSearch = '';
  let currentWardenFilter = 'all';
  let currentWardenCategory = 'all';
  let currentWardenHostel = 'all';
  let currentWardenSearch = '';

  // Wizard draft state
  let wizardData = {
    category: 'Electrical',
    priority: 'Medium',
    title: '',
    description: '',
    preferredSlot: 'Morning (9:00 AM - 12:00 PM)',
    images: ['https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=500&auto=format&fit=crop&q=60']
  };
  let currentWizardStep = 1;

  // Active modal ticket tracking
  let activeTimelineTicketId = null;
  let activeEscalateTicketId = null;
  let activeConfirmTicketId = null;
  let activeWardenManageTicketId = null;
  let selectedStarRating = 5;

  // Init app
  init();

  function init() {
    setupEventListeners();
    store.subscribe(renderApp);
    renderApp(store.state);
  }

  // ==========================================================================
  // MAIN RENDER CONTROLLER
  // ==========================================================================
  function renderApp(state = store.state) {
    const user = state.currentUser;

    // 1. Update Navigation Bar Header
    const userDropdownBtn = document.getElementById('btn-user-dropdown');
    const navUserAvatar = document.getElementById('nav-user-avatar');
    const navUserName = document.getElementById('nav-user-name');
    const notifDot = document.getElementById('notif-unread-dot');

    if (user) {
      userDropdownBtn.style.display = 'flex';
      navUserAvatar.textContent = user.avatar || 'US';
      navUserName.textContent = user.name;
    } else {
      userDropdownBtn.style.display = 'none';
    }

    const unreadCount = state.notifications.filter(n => !n.read).length;
    if (notifDot) {
      notifDot.style.display = unreadCount > 0 ? 'block' : 'none';
    }

    // 2. View Routing
    const viewAuth = document.getElementById('view-auth');
    const viewStudent = document.getElementById('view-student');
    const viewWarden = document.getElementById('view-warden');

    viewAuth.style.display = 'none';
    viewStudent.style.display = 'none';
    viewWarden.style.display = 'none';

    if (!user) {
      viewAuth.style.display = 'block';
    } else if (user.role === 'student') {
      viewStudent.style.display = 'block';
      renderStudentPortal(state);
    } else if (user.role === 'warden') {
      viewWarden.style.display = 'block';
      renderWardenPortal(state);
    }
  }

  // ==========================================================================
  // STUDENT PORTAL RENDERER
  // ==========================================================================
  function renderStudentPortal(state) {
    const user = state.currentUser;

    // Header info
    document.getElementById('student-display-name').textContent = user.name;
    document.getElementById('student-badge-roll').textContent = user.rollNo || 'ST20230042';
    document.getElementById('student-badge-room').textContent = user.hostelRoomDisplay || `${user.hostel}, ${user.room}`;
    document.getElementById('student-badge-email').textContent = user.email;

    // Stats
    const stats = store.getStats();
    document.getElementById('stat-student-active').textContent = stats.pending + stats.inProgress;
    document.getElementById('stat-student-resolved').textContent = stats.resolved;
    document.getElementById('stat-student-escalated').textContent = stats.escalated;

    // Complaints list filtering
    let complaints = state.complaints.filter(c => c.studentId === user.id);

    if (currentStudentFilter === 'pending') {
      complaints = complaints.filter(c => c.status === 'Submitted' || c.status === 'Under Review');
    } else if (currentStudentFilter === 'in_progress') {
      complaints = complaints.filter(c => c.status === 'Assigned' || c.status === 'In Progress');
    } else if (currentStudentFilter === 'escalated') {
      complaints = complaints.filter(c => c.escalated || c.status === 'Escalated');
    } else if (currentStudentFilter === 'resolved') {
      complaints = complaints.filter(c => c.status === 'Resolved' || c.status === 'Closed');
    }

    if (currentStudentSearch.trim()) {
      const q = currentStudentSearch.toLowerCase();
      complaints = complaints.filter(c => 
        c.id.toLowerCase().includes(q) || 
        c.title.toLowerCase().includes(q) || 
        c.category.toLowerCase().includes(q)
      );
    }

    const container = document.getElementById('student-complaints-list');

    if (complaints.length === 0) {
      container.innerHTML = `
        <div class="glass-card" style="text-align: center; padding: 3rem 1.5rem;">
          <i class="fa-solid fa-clipboard-check" style="font-size: 2.5rem; color: var(--text-subtle); margin-bottom: 0.75rem;"></i>
          <h3 style="font-size: 1.1rem; margin-bottom: 0.35rem;">No Complaints Found</h3>
          <p style="color: var(--text-muted); font-size: 0.88rem;">There are no complaints matching your selected criteria.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = complaints.map(c => renderComplaintCard(c)).join('');

    // Bind card action buttons
    container.querySelectorAll('.btn-view-timeline').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.dataset.id;
        openTimelineModal(id);
      });
    });

    container.querySelectorAll('.btn-open-escalate').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.dataset.id;
        openEscalateModal(id);
      });
    });

    container.querySelectorAll('.btn-open-confirm-res').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.dataset.id;
        openConfirmResolutionModal(id);
      });
    });
  }

  function renderComplaintCard(c) {
    const statusClass = c.status.toLowerCase().replace(/\s+/g, '_');
    const priorityClass = c.priority.toLowerCase();
    const createdFormatted = new Date(c.createdAt).toLocaleDateString('en-IN', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });

    let statusText = c.status;
    if (c.escalated) statusText = '🚨 Escalated';

    const isResolvedPending = c.status === 'Resolved' && c.studentConfirmed === null;

    return `
      <div class="complaint-card">
        <div class="complaint-card-header">
          <div>
            <div class="complaint-meta-top">
              <span class="ticket-id-tag">${c.id}</span>
              <span class="status-badge ${statusClass}">
                <i class="fa-solid fa-circle" style="font-size: 0.5rem;"></i>
                ${statusText}
              </span>
              <span class="priority-badge ${priorityClass}">${c.priority} Priority</span>
            </div>
            <div class="complaint-title-block" style="margin-top: 0.5rem;">
              <h3>${escapeHtml(c.title)}</h3>
            </div>
          </div>
          <span style="font-size: 0.78rem; color: var(--text-subtle);">${createdFormatted}</span>
        </div>

        <div class="complaint-card-body">
          <p>${escapeHtml(c.description)}</p>
        </div>

        <div class="complaint-details-grid">
          <div class="complaint-detail-item">
            <i class="fa-solid fa-layer-group"></i>
            <span>${c.category} (${c.subcategory || 'General'})</span>
          </div>
          <div class="complaint-detail-item">
            <i class="fa-solid fa-clock"></i>
            <span>Slot: ${c.preferredSlot}</span>
          </div>
          ${c.assignedTechnicianName ? `
            <div class="tech-info-pill">
              <i class="fa-solid fa-user-gear"></i>
              <span>Assigned: <strong>${c.assignedTechnicianName}</strong></span>
            </div>
          ` : '<span style="color: var(--text-subtle);">Waiting for staff assignment...</span>'}
        </div>

        ${isResolvedPending ? `
          <div class="resolution-prompt-box">
            <div class="resolution-prompt-text">
              <i class="fa-solid fa-circle-info"></i>
              <span>Technician marked this issue as Resolved. Please confirm repair:</span>
            </div>
            <button class="btn-card-action resolve-confirm btn-open-confirm-res" data-id="${c.id}">
              <i class="fa-solid fa-clipboard-check"></i>
              <span>Verify & Confirm</span>
            </button>
          </div>
        ` : ''}

        <div class="complaint-card-actions">
          <button class="btn-card-action btn-view-timeline" data-id="${c.id}">
            <i class="fa-solid fa-timeline"></i>
            <span>View Live Stepper Timeline</span>
          </button>

          <div class="action-btns-group">
            ${(!c.escalated && c.status !== 'Resolved' && c.status !== 'Closed') ? `
              <button class="btn-card-action escalate btn-open-escalate" data-id="${c.id}">
                <i class="fa-solid fa-triangle-exclamation"></i>
                <span>Escalate to Warden</span>
              </button>
            ` : ''}
          </div>
        </div>
      </div>
    `;
  }

  // ==========================================================================
  // HOSTEL WARDEN PORTAL RENDERER
  // ==========================================================================
  function renderWardenPortal(state) {
    const stats = store.getStats();
    document.getElementById('stat-warden-total').textContent = state.complaints.length;
    document.getElementById('stat-warden-pending').textContent = state.complaints.filter(c => c.status === 'Submitted' || c.status === 'Under Review').length;
    document.getElementById('stat-warden-progress').textContent = state.complaints.filter(c => c.status === 'Assigned' || c.status === 'In Progress').length;
    document.getElementById('stat-warden-escalated').textContent = state.complaints.filter(c => c.escalated || c.status === 'Escalated').length;
    document.getElementById('stat-warden-resolved').textContent = state.complaints.filter(c => c.status === 'Resolved' || c.status === 'Closed').length;

    // Render Urgent Escalation Banner
    const urgentTickets = state.complaints.filter(c => c.escalated || c.status === 'Escalated');
    const urgentContainer = document.getElementById('urgent-tickets-list-container');
    const urgentBanner = document.getElementById('urgent-escalations-banner');

    if (urgentTickets.length === 0) {
      urgentBanner.style.display = 'none';
    } else {
      urgentBanner.style.display = 'flex';
      urgentContainer.innerHTML = urgentTickets.map(t => `
        <div class="urgent-ticket-item">
          <div class="urgent-item-info">
            <strong>Ticket #${t.id} — ${escapeHtml(t.title)}</strong>
            <span>Student: ${t.studentName} (${t.room}) • Reason: "${escapeHtml(t.escalationReason || 'Delayed response')}"</span>
          </div>
          <button class="btn-submit-primary btn-open-warden-manage" data-id="${t.id}" style="width: auto; padding: 0.4rem 0.85rem; font-size: 0.8rem; background: var(--accent-rose);">
            <i class="fa-solid fa-bolt"></i>
            <span>Assign Urgently</span>
          </button>
        </div>
      `).join('');
    }

    // Warden Complaints Table
    let tickets = state.complaints;

    if (currentWardenFilter === 'pending') {
      tickets = tickets.filter(c => c.status === 'Submitted' || c.status === 'Under Review');
    } else if (currentWardenFilter === 'in_progress') {
      tickets = tickets.filter(c => c.status === 'Assigned' || c.status === 'In Progress');
    } else if (currentWardenFilter === 'escalated') {
      tickets = tickets.filter(c => c.escalated || c.status === 'Escalated');
    } else if (currentWardenFilter === 'resolved') {
      tickets = tickets.filter(c => c.status === 'Resolved' || c.status === 'Closed');
    }

    if (currentWardenCategory !== 'all') {
      tickets = tickets.filter(c => c.category === currentWardenCategory);
    }

    if (currentWardenHostel !== 'all') {
      tickets = tickets.filter(c => c.room.includes(currentWardenHostel));
    }

    if (currentWardenSearch.trim()) {
      const q = currentWardenSearch.toLowerCase();
      tickets = tickets.filter(c => 
        c.id.toLowerCase().includes(q) || 
        c.studentName.toLowerCase().includes(q) || 
        c.room.toLowerCase().includes(q) || 
        c.title.toLowerCase().includes(q)
      );
    }

    const tbody = document.getElementById('warden-table-body');

    if (tickets.length === 0) {
      tbody.innerHTML = `
        <tr>
          <td colspan="7" style="text-align: center; padding: 2rem; color: var(--text-muted);">
            No maintenance tickets found for current filters.
          </td>
        </tr>
      `;
      return;
    }

    tbody.innerHTML = tickets.map(t => {
      const statusClass = t.status.toLowerCase().replace(/\s+/g, '_');
      const priorityClass = t.priority.toLowerCase();

      return `
        <tr>
          <td><span class="ticket-id-tag">${t.id}</span></td>
          <td class="student-info-cell">
            <strong>${escapeHtml(t.studentName)}</strong>
            <span>${escapeHtml(t.room)}</span>
          </td>
          <td>
            <strong>${escapeHtml(t.title)}</strong>
            <span style="font-size: 0.75rem; color: var(--text-subtle); display: block;">${t.category}</span>
          </td>
          <td><span class="priority-badge ${priorityClass}">${t.priority}</span></td>
          <td><span class="status-badge ${statusClass}">${t.escalated ? '🚨 Escalated' : t.status}</span></td>
          <td>
            ${t.assignedTechnicianName 
              ? `<span style="font-size: 0.82rem; font-weight: 600;">${t.assignedTechnicianName}</span>` 
              : '<span style="color: var(--text-subtle); font-size: 0.78rem;">Unassigned</span>'}
          </td>
          <td>
            <button class="btn-card-action btn-open-warden-manage" data-id="${t.id}" style="padding: 0.35rem 0.7rem; font-size: 0.78rem;">
              <i class="fa-solid fa-pen-to-square"></i>
              <span>Manage</span>
            </button>
          </td>
        </tr>
      `;
    }).join('');

    // Bind warden table manage buttons
    document.querySelectorAll('.btn-open-warden-manage').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.dataset.id;
        openWardenManageModal(id);
      });
    });
  }

  // ==========================================================================
  // EVENT LISTENERS & HANDLERS
  // ==========================================================================
  function setupEventListeners() {
    // 1. Navigation & Presets
    const userDropdownBtn = document.getElementById('btn-user-dropdown');
    const presetMenu = document.getElementById('user-preset-menu');

    userDropdownBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      presetMenu.classList.toggle('active');
    });

    document.addEventListener('click', () => {
      presetMenu.classList.remove('active');
    });

    document.querySelectorAll('.preset-option[data-userid]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const userId = e.currentTarget.dataset.userid;
        store.quickFillUser(userId);
        showToast('Profile Switched', `Active session: ${store.currentUser.name}`, 'info');
      });
    });

    document.getElementById('btn-nav-logout').addEventListener('click', () => {
      store.logout();
      showToast('Logged Out', 'Session terminated.', 'info');
    });

    // Brand logo click -> go to overview
    document.getElementById('btn-brand-home').addEventListener('click', (e) => {
      e.preventDefault();
      renderApp();
    });

    // 2. Auth Hub Tabs & Quick Fill Presets
    document.querySelectorAll('.auth-tab-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        document.querySelectorAll('.auth-tab-btn').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');

        const tab = e.target.dataset.tab;
        document.getElementById('form-student-login').style.display = tab === 'student-login' ? 'block' : 'none';
        document.getElementById('form-student-signup').style.display = tab === 'student-signup' ? 'block' : 'none';
        document.getElementById('form-warden-login').style.display = tab === 'warden-login' ? 'block' : 'none';
      });
    });

    document.querySelectorAll('.btn-preset-quick').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const userId = e.currentTarget.dataset.demo;
        store.quickFillUser(userId);
        showToast('Demo Preset Loaded', `Logged in as ${store.currentUser.name}`, 'success');
      });
    });

    // Form submits
    document.getElementById('form-student-login').addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('login-email').value;
      const pass = document.getElementById('login-password').value;
      try {
        store.login(email, pass);
        showToast('Welcome Back!', `Logged in as ${store.currentUser.name}`, 'success');
      } catch (err) {
        showToast('Login Failed', err.message, 'danger');
      }
    });

    document.getElementById('form-student-signup').addEventListener('submit', (e) => {
      e.preventDefault();
      try {
        const newUser = store.registerUser({
          name: document.getElementById('signup-name').value,
          rollNo: document.getElementById('signup-roll').value,
          email: document.getElementById('signup-email').value,
          hostel: document.getElementById('signup-hostel').value,
          room: document.getElementById('signup-room').value,
          password: document.getElementById('signup-password').value
        });
        showToast('Account Registered', `Welcome to VUFIX, ${newUser.name}!`, 'success');
      } catch (err) {
        showToast('Registration Error', err.message, 'danger');
      }
    });

    document.getElementById('form-warden-login').addEventListener('submit', (e) => {
      e.preventDefault();
      const adminId = document.getElementById('warden-admin-id').value;
      const pass = document.getElementById('warden-password').value;
      try {
        store.login(adminId, pass);
        showToast('Warden Authenticated', 'Control Center Unlocked.', 'success');
      } catch (err) {
        showToast('Warden Login Error', err.message, 'danger');
      }
    });

    // 3. Student Filter & Search
    document.getElementById('student-filter-pills').addEventListener('click', (e) => {
      if (e.target.classList.contains('btn-filter-pill')) {
        document.querySelectorAll('#student-filter-pills .btn-filter-pill').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        currentStudentFilter = e.target.dataset.filter;
        renderStudentPortal(store.state);
      }
    });

    document.getElementById('search-student-complaints').addEventListener('input', (e) => {
      currentStudentSearch = e.target.value;
      renderStudentPortal(store.state);
    });

    // 4. Warden Filter & Search
    document.getElementById('warden-filter-pills').addEventListener('click', (e) => {
      if (e.target.classList.contains('btn-filter-pill')) {
        document.querySelectorAll('#warden-filter-pills .btn-filter-pill').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        currentWardenFilter = e.target.dataset.wardenfilter;
        renderWardenPortal(store.state);
      }
    });

    document.getElementById('filter-warden-category').addEventListener('change', (e) => {
      currentWardenCategory = e.target.value;
      renderWardenPortal(store.state);
    });

    document.getElementById('filter-warden-hostel').addEventListener('change', (e) => {
      currentWardenHostel = e.target.value;
      renderWardenPortal(store.state);
    });

    document.getElementById('search-warden-complaints').addEventListener('input', (e) => {
      currentWardenSearch = e.target.value;
      renderWardenPortal(store.state);
    });

    // 5. Wizard Modal Logic
    document.getElementById('btn-open-complaint-wizard').addEventListener('click', () => {
      openWizardModal();
    });

    document.querySelectorAll('.close-wizard').forEach(btn => {
      btn.addEventListener('click', () => closeWizardModal());
    });

    document.querySelectorAll('.category-option-card').forEach(card => {
      card.addEventListener('click', (e) => {
        document.querySelectorAll('.category-option-card').forEach(c => c.classList.remove('selected'));
        const target = e.currentTarget;
        target.classList.add('selected');
        wizardData.category = target.dataset.cat;
      });
    });

    document.querySelectorAll('.priority-radio-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        document.querySelectorAll('.priority-radio-btn').forEach(b => b.classList.remove('selected'));
        const target = e.currentTarget;
        target.classList.add('selected');
        wizardData.priority = target.dataset.val;
      });
    });

    document.querySelectorAll('.sample-img-thumb').forEach(img => {
      img.addEventListener('click', (e) => {
        document.querySelectorAll('.sample-img-thumb').forEach(i => i.classList.remove('selected'));
        e.target.classList.add('selected');
        wizardData.images = [e.target.dataset.url];
      });
    });

    document.getElementById('btn-wiz-next').addEventListener('click', () => {
      if (currentWizardStep === 1) {
        currentWizardStep = 2;
        renderWizardStep();
      } else if (currentWizardStep === 2) {
        const title = document.getElementById('wiz-title').value.trim();
        const desc = document.getElementById('wiz-description').value.trim();
        if (!title || !desc) {
          showToast('Form Incomplete', 'Please enter a title and description.', 'warning');
          return;
        }
        wizardData.title = title;
        wizardData.description = desc;
        wizardData.preferredSlot = document.getElementById('wiz-slot').value;
        currentWizardStep = 3;
        renderWizardStep();
      } else if (currentWizardStep === 3) {
        // Submit
        try {
          const newTicket = store.createComplaint(wizardData);
          closeWizardModal();
          showToast('Complaint Filed!', `Ticket #${newTicket.id} successfully created.`, 'success');
        } catch (err) {
          showToast('Error', err.message, 'danger');
        }
      }
    });

    document.getElementById('btn-wiz-prev').addEventListener('click', () => {
      if (currentWizardStep > 1) {
        currentWizardStep--;
        renderWizardStep();
      }
    });

    // 6. Timeline Modal Closes
    document.getElementById('close-timeline').addEventListener('click', closeTimelineModal);
    document.getElementById('btn-timeline-close').addEventListener('click', closeTimelineModal);

    // 7. Escalation Modal Handlers
    document.getElementById('close-escalate').addEventListener('click', closeEscalateModal);
    document.getElementById('btn-cancel-escalate').addEventListener('click', closeEscalateModal);
    document.getElementById('btn-submit-escalate').addEventListener('click', () => {
      const selectedRadio = document.querySelector('input[name="esc-reason"]:checked');
      const customText = document.getElementById('escalate-custom-text').value.trim();
      let reason = selectedRadio ? selectedRadio.value : 'Delayed response';
      if (customText) reason += ` - ${customText}`;

      try {
        store.escalateComplaint(activeEscalateTicketId, reason);
        closeEscalateModal();
        showToast('🚨 Ticket Escalated', 'High priority flag sent to Warden Rinu Babu.', 'warning');
      } catch (err) {
        showToast('Error', err.message, 'danger');
      }
    });

    // 8. Confirmation Resolution Modal Handlers
    document.getElementById('close-confirm-res').addEventListener('click', closeConfirmResolutionModal);
    document.getElementById('btn-res-yes').addEventListener('click', () => {
      const feedbackBox = document.getElementById('rating-feedback-box');
      if (feedbackBox.style.display === 'none') {
        feedbackBox.style.display = 'block';
        return;
      }
      const comment = document.getElementById('res-feedback-text').value.trim();
      store.confirmResolution(activeConfirmTicketId, true, { rating: selectedStarRating, comment });
      closeConfirmResolutionModal();
      showToast('Verified & Closed', 'Thank you for confirming resolution!', 'success');
    });

    document.getElementById('btn-res-no').addEventListener('click', () => {
      const comment = document.getElementById('res-feedback-text').value.trim();
      store.confirmResolution(activeConfirmTicketId, false, { comment });
      closeConfirmResolutionModal();
      showToast('Ticket Reopened', 'Warden has been notified that issue remains unresolved.', 'warning');
    });

    document.querySelectorAll('#star-rating-picker i').forEach(star => {
      star.addEventListener('click', (e) => {
        selectedStarRating = parseInt(e.target.dataset.star, 10);
        document.querySelectorAll('#star-rating-picker i').forEach((s, idx) => {
          s.style.color = idx < selectedStarRating ? '#f59e0b' : 'var(--text-subtle)';
        });
      });
    });

    // 9. Warden Management Modal Handlers
    document.getElementById('close-warden-manage').addEventListener('click', closeWardenManageModal);
    document.getElementById('btn-warden-cancel').addEventListener('click', closeWardenManageModal);
    document.getElementById('btn-warden-save-ticket').addEventListener('click', () => {
      if (!activeWardenManageTicketId) return;

      const status = document.getElementById('wm-status-select').value;
      const techId = document.getElementById('wm-tech-select').value;
      const eta = document.getElementById('wm-eta-input').value;
      const note = document.getElementById('wm-note-input').value.trim();

      try {
        store.updateComplaintWarden(activeWardenManageTicketId, {
          status,
          technicianId: techId || undefined,
          eta: eta ? new Date(eta).toISOString() : undefined,
          note: note || undefined
        });

        closeWardenManageModal();
        showToast('Ticket Updated', `Changes saved for #${activeWardenManageTicketId}.`, 'success');
      } catch (err) {
        showToast('Update Error', err.message, 'danger');
      }
    });

    // 10. Research Overlay Modal
    document.getElementById('btn-toggle-research').addEventListener('click', () => {
      document.getElementById('modal-research').classList.add('active');
    });
    document.getElementById('close-research').addEventListener('click', () => {
      document.getElementById('modal-research').classList.remove('active');
    });
  }

  // ==========================================================================
  // WIZARD MODAL CONTROLLER
  // ==========================================================================
  function openWizardModal() {
    currentWizardStep = 1;
    renderWizardStep();
    document.getElementById('modal-complaint-wizard').classList.add('active');
  }

  function closeWizardModal() {
    document.getElementById('modal-complaint-wizard').classList.remove('active');
  }

  function renderWizardStep() {
    document.getElementById('wizard-step-1-content').style.display = currentWizardStep === 1 ? 'block' : 'none';
    document.getElementById('wizard-step-2-content').style.display = currentWizardStep === 2 ? 'block' : 'none';
    document.getElementById('wizard-step-3-content').style.display = currentWizardStep === 3 ? 'block' : 'none';

    document.getElementById('node-step-1').className = 'wizard-step-node' + (currentWizardStep >= 1 ? ' active' : '');
    document.getElementById('node-step-2').className = 'wizard-step-node' + (currentWizardStep >= 2 ? ' active' : '');
    document.getElementById('node-step-3').className = 'wizard-step-node' + (currentWizardStep >= 3 ? ' active' : '');

    document.getElementById('btn-wiz-prev').style.display = currentWizardStep > 1 ? 'inline-block' : 'none';
    
    const nextBtn = document.getElementById('btn-wiz-next');
    if (currentWizardStep === 3) {
      nextBtn.querySelector('span').textContent = 'Submit Complaint';
      nextBtn.querySelector('i').className = 'fa-solid fa-paper-plane';

      // Summary preview
      document.getElementById('summary-category').textContent = wizardData.category;
      document.getElementById('summary-priority').textContent = wizardData.priority + ' Priority';
      document.getElementById('summary-priority').className = 'priority-badge ' + wizardData.priority.toLowerCase();
      document.getElementById('summary-title').textContent = wizardData.title;
      const user = store.currentUser;
      document.getElementById('summary-location').textContent = user ? (user.hostelRoomDisplay || user.room) : 'Hostel A';
      document.getElementById('summary-slot').textContent = wizardData.preferredSlot;
    } else {
      nextBtn.querySelector('span').textContent = 'Continue';
      nextBtn.querySelector('i').className = 'fa-solid fa-arrow-right';
    }
  }

  // ==========================================================================
  // TIMELINE MODAL CONTROLLER
  // ==========================================================================
  function openTimelineModal(ticketId) {
    activeTimelineTicketId = ticketId;
    const ticket = store.complaints.find(c => c.id === ticketId);
    if (!ticket) return;

    document.getElementById('timeline-ticket-id').textContent = ticket.id;
    document.getElementById('timeline-ticket-title').textContent = ticket.title;

    const statusBadge = document.getElementById('timeline-status-badge');
    statusBadge.textContent = ticket.escalated ? '🚨 Escalated' : ticket.status;
    statusBadge.className = 'status-badge ' + ticket.status.toLowerCase().replace(/\s+/g, '_');

    // Tech card
    const techBox = document.getElementById('timeline-tech-box');
    if (ticket.assignedTechnicianName) {
      techBox.style.display = 'flex';
      document.getElementById('timeline-tech-avatar').textContent = ticket.assignedTechnicianAvatar || 'TK';
      document.getElementById('timeline-tech-name').textContent = ticket.assignedTechnicianName;
      document.getElementById('timeline-tech-specialty').textContent = ticket.assignedTechnicianSpecialty || 'Specialist';
      document.getElementById('timeline-tech-phone').href = 'tel:' + (ticket.assignedTechnicianPhone || '');
    } else {
      techBox.style.display = 'none';
    }

    // ETA display
    const etaText = document.getElementById('timeline-eta-text');
    if (ticket.eta) {
      etaText.textContent = new Date(ticket.eta).toLocaleString('en-IN', { dateStyle: 'medium', timeStyle: 'short' });
    } else {
      etaText.textContent = 'ETA to be assigned by Warden';
    }

    // Render Timeline Stepper Nodes
    const stepperContainer = document.getElementById('stepper-timeline-container');
    stepperContainer.innerHTML = ticket.timeline.map((log, idx) => {
      const isLast = idx === ticket.timeline.length - 1;
      const logDateFormatted = new Date(log.timestamp).toLocaleString('en-IN', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });

      let icon = 'fa-check';
      if (log.type === 'submitted') icon = 'fa-paper-plane';
      else if (log.type === 'review') icon = 'fa-eye';
      else if (log.type === 'assigned') icon = 'fa-user-check';
      else if (log.type === 'in_progress') icon = 'fa-gears';
      else if (log.type === 'escalated') icon = 'fa-triangle-exclamation';
      else if (log.type === 'resolved') icon = 'fa-circle-check';
      else if (log.type === 'closed') icon = 'fa-lock';

      return `
        <div class="timeline-node ${isLast ? 'active' : 'completed'}">
          <div class="timeline-node-icon">
            <i class="fa-solid ${icon}"></i>
          </div>
          <div class="timeline-content-card">
            <div class="timeline-meta">
              <strong>${escapeHtml(log.title)}</strong>
              <span>${logDateFormatted}</span>
            </div>
            <div class="timeline-body-text">${escapeHtml(log.text)}</div>
            <span class="timeline-author-tag">By: ${escapeHtml(log.author)}</span>
          </div>
        </div>
      `;
    }).join('');

    document.getElementById('modal-timeline').classList.add('active');
  }

  function closeTimelineModal() {
    document.getElementById('modal-timeline').classList.remove('active');
  }

  // ==========================================================================
  // ESCALATION MODAL CONTROLLER
  // ==========================================================================
  function openEscalateModal(ticketId) {
    activeEscalateTicketId = ticketId;
    document.getElementById('escalate-ticket-id').textContent = '#' + ticketId;
    document.getElementById('escalate-custom-text').value = '';
    document.getElementById('modal-escalate').classList.add('active');
  }

  function closeEscalateModal() {
    document.getElementById('modal-escalate').classList.remove('active');
  }

  // ==========================================================================
  // CONFIRM RESOLUTION MODAL CONTROLLER
  // ==========================================================================
  function openConfirmResolutionModal(ticketId) {
    activeConfirmTicketId = ticketId;
    document.getElementById('confirm-ticket-id').textContent = '#' + ticketId;
    document.getElementById('rating-feedback-box').style.display = 'none';
    document.getElementById('res-feedback-text').value = '';
    document.getElementById('modal-confirm-resolution').classList.add('active');
  }

  function closeConfirmResolutionModal() {
    document.getElementById('modal-confirm-resolution').classList.remove('active');
  }

  // ==========================================================================
  // WARDEN MANAGE MODAL CONTROLLER
  // ==========================================================================
  function openWardenManageModal(ticketId) {
    activeWardenManageTicketId = ticketId;
    const ticket = store.complaints.find(c => c.id === ticketId);
    if (!ticket) return;

    document.getElementById('warden-manage-ticket-id').textContent = '#' + ticket.id;
    document.getElementById('wm-student-name').textContent = ticket.studentName;
    document.getElementById('wm-student-room').textContent = ticket.room;
    document.getElementById('wm-issue-title').textContent = ticket.title;

    document.getElementById('wm-status-select').value = ticket.status;
    document.getElementById('wm-tech-select').value = ticket.assignedTechnicianId || '';
    
    if (ticket.eta) {
      const d = new Date(ticket.eta);
      const isoStr = new Date(d.getTime() - d.getTimezoneOffset() * 60000).toISOString().slice(0, 16);
      document.getElementById('wm-eta-input').value = isoStr;
    } else {
      document.getElementById('wm-eta-input').value = '';
    }

    document.getElementById('wm-note-input').value = '';
    document.getElementById('modal-warden-manage').classList.add('active');
  }

  function closeWardenManageModal() {
    document.getElementById('modal-warden-manage').classList.remove('active');
  }

  // ==========================================================================
  // TOAST NOTIFICATION SYSTEM
  // ==========================================================================
  function showToast(title, message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `vufix-toast ${type}`;

    let icon = 'fa-circle-info';
    if (type === 'success') icon = 'fa-circle-check';
    else if (type === 'warning') icon = 'fa-triangle-exclamation';
    else if (type === 'danger') icon = 'fa-circle-xmark';

    toast.innerHTML = `
      <i class="fa-solid ${icon}" style="font-size: 1.1rem; margin-top: 0.1rem;"></i>
      <div class="toast-content">
        <strong>${escapeHtml(title)}</strong>
        <p>${escapeHtml(message)}</p>
      </div>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 4000);
  }

  // Helper escape
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
});
