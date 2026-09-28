import os

css_content = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --primary: #4f46e5;
  --primary-hover: #4338ca;
  --primary-light: #e0e7ff;
  
  --bg-main: #f8fafc;
  --bg-card: #ffffff;
  --bg-sidebar: #ffffff;
  
  --text-dark: #0f172a;
  --text-gray: #64748b;
  --text-light: #94a3b8;
  
  --border: #e2e8f0;
  
  --success: #22c55e;
  --success-bg: #dcfce7;
  --danger: #ef4444;
  --danger-bg: #fee2e2;
  --warning: #f59e0b;
  --warning-bg: #fef3c7;
  --info: #3b82f6;
  --info-bg: #dbeafe;
  
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
}

body {
  background-color: var(--bg-main);
  color: var(--text-dark);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* ================= AUTH VIEW ================= */
.auth-wrapper {
  min-height: 100vh;
  background-color: #2e2c54; /* Dark purple background */
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.auth-card {
  background: white;
  border-radius: 16px;
  width: 100%;
  max-width: 480px;
  padding: 2.5rem;
  box-shadow: var(--shadow-lg);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.auth-logo {
  width: 48px;
  height: 48px;
  background: var(--primary-light);
  color: var(--primary);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.auth-card h1 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.auth-card p {
  color: var(--text-gray);
  font-size: 0.875rem;
  text-align: center;
  margin-bottom: 2rem;
}

.auth-tabs {
  display: flex;
  width: 100%;
  background: var(--bg-main);
  border-radius: 8px;
  padding: 0.25rem;
  margin-bottom: 1.5rem;
}

.auth-tab-btn {
  flex: 1;
  padding: 0.5rem;
  border: none;
  background: transparent;
  color: var(--text-gray);
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.auth-tab-btn.active {
  background: white;
  color: var(--primary);
  box-shadow: var(--shadow-sm);
}

.auth-form {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-dark);
}

.form-control {
  padding: 0.75rem 1rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 0.875rem;
  outline: none;
  transition: border-color 0.2s;
}

.form-control:focus {
  border-color: var(--primary);
}

.btn-primary {
  background: var(--primary);
  color: white;
  border: none;
  padding: 0.875rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  transition: background 0.2s;
  width: 100%;
}

.btn-primary:hover {
  background: var(--primary-hover);
}

.demo-presets {
  margin-top: 2rem;
  width: 100%;
}

.demo-presets-title {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--text-gray);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.preset-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.preset-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: transparent;
  cursor: pointer;
  transition: all 0.2s;
  text-align: left;
}

.preset-item:hover {
  background: var(--bg-main);
  border-color: #cbd5e1;
}

.preset-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.preset-icon {
  color: var(--primary);
  font-size: 1rem;
}

.preset-name {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-dark);
}

.preset-id {
  font-size: 0.75rem;
  color: var(--text-gray);
}

/* ================= APP LAYOUT ================= */
.app-layout {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 260px;
  background: var(--bg-sidebar);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
}

.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.5rem;
  border-bottom: 1px solid var(--border);
}

.sidebar-brand .logo {
  width: 32px;
  height: 32px;
  background: var(--primary-light);
  color: var(--primary);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
}

.sidebar-brand h2 {
  font-size: 1.25rem;
  font-weight: 700;
}

.sidebar-nav {
  padding: 1rem 0;
  flex: 1;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1.5rem;
  color: var(--text-gray);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  border-left: 3px solid transparent;
}

.nav-item:hover {
  background: var(--bg-main);
  color: var(--text-dark);
}

.nav-item.active {
  background: var(--primary-light);
  color: var(--primary);
  border-left-color: var(--primary);
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding: 2rem;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
}

.welcome-section h1 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.user-tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.user-tag {
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 0.25rem 0.75rem;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--text-gray);
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: var(--shadow-sm);
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
}

.stat-info h3 {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-gray);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.25rem;
}

.stat-info p {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-dark);
}

.stat-card.primary { border-color: var(--primary-light); }
.stat-card.primary .stat-icon { background: var(--primary-light); color: var(--primary); }

.stat-card.success { border-color: var(--success-bg); }
.stat-card.success .stat-icon { background: var(--success-bg); color: var(--success); }

.stat-card.danger { border-color: var(--danger-bg); }
.stat-card.danger .stat-icon { background: var(--danger-bg); color: var(--danger); }

.stat-card.warning { border-color: var(--warning-bg); }
.stat-card.warning .stat-icon { background: var(--warning-bg); color: var(--warning); }

.stat-card.info { border-color: var(--info-bg); }
.stat-card.info .stat-icon { background: var(--info-bg); color: var(--info); }

/* ================= BADGES ================= */
.badge {
  padding: 0.25rem 0.75rem;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.badge.danger { background: var(--danger-bg); color: var(--danger); }
.badge.info { background: var(--info-bg); color: var(--info); }
.badge.warning { background: var(--warning-bg); color: var(--warning); }
.badge.success { background: var(--success-bg); color: var(--success); }

.priority-high { color: var(--danger); font-size: 0.75rem; font-weight: 600; }
.priority-medium { color: var(--warning); font-size: 0.75rem; font-weight: 600; }
.priority-low { color: var(--info); font-size: 0.75rem; font-weight: 600; }

/* ================= CARDS / LISTS ================= */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.section-header h2 {
  font-size: 1.125rem;
  font-weight: 700;
}

.complaints-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.complaint-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.25rem;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}

.complaint-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.75rem;
}

.complaint-id {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--text-gray);
  margin-bottom: 0.25rem;
}

.complaint-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-dark);
}

.complaint-desc {
  font-size: 0.875rem;
  color: var(--text-gray);
  margin-bottom: 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.complaint-footer {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.complaint-meta {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.75rem;
  color: var(--text-gray);
}

.complaint-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 0.75rem;
  border-top: 1px solid var(--border);
}

/* ================= WARDEN TABLE ================= */
.alert-banner {
  background: var(--danger-bg);
  border: 1px solid #fca5a5;
  border-radius: 8px;
  padding: 1rem 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.alert-banner .alert-content {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: var(--danger);
  font-weight: 600;
  font-size: 0.875rem;
}

.alert-banner .alert-desc {
  color: #7f1d1d;
  font-weight: 400;
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.btn-danger-sm {
  background: var(--danger);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
}

.table-container {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
  overflow: hidden;
}

.table-header-actions {
  padding: 1rem 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border);
}

.table-tabs {
  display: flex;
  gap: 0.5rem;
}

.table-tab {
  padding: 0.5rem 1rem;
  border: none;
  background: transparent;
  color: var(--text-gray);
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 100px;
  cursor: pointer;
}

.table-tab.active {
  background: var(--primary);
  color: white;
}

.filter-select {
  padding: 0.5rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  font-size: 0.875rem;
  outline: none;
  background: white;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 1rem 1.25rem;
  text-align: left;
  font-size: 0.875rem;
  border-bottom: 1px solid var(--border);
}

th {
  font-weight: 600;
  color: var(--text-gray);
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 0.05em;
}

tr:last-child td {
  border-bottom: none;
}

.td-student {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.td-student strong { color: var(--text-dark); }
.td-student span { color: var(--text-gray); font-size: 0.75rem; }

.td-category {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.td-category strong { color: var(--text-dark); }
.td-category span { color: var(--text-gray); font-size: 0.75rem; display: flex; align-items: center; gap: 0.25rem; }

.staff-avatar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.avatar-circle {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--primary-light);
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.65rem;
  font-weight: 700;
}

.btn-manage {
  background: var(--primary);
  color: white;
  border: none;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.btn-icon {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-gray);
  padding: 0.35rem;
  border-radius: 6px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* ================= WIZARD ================= */
.wizard-container {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
  box-shadow: var(--shadow-sm);
}

.wizard-stepper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2.5rem;
  position: relative;
}

.wizard-stepper::before {
  content: '';
  position: absolute;
  top: 16px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--border);
  z-index: 1;
}

.wizard-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  position: relative;
  z-index: 2;
  background: var(--bg-card);
  padding: 0 1rem;
}

.step-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: white;
  border: 2px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-gray);
}

.wizard-step.active .step-circle {
  background: var(--primary);
  border-color: var(--primary);
  color: white;
}
.wizard-step.completed .step-circle {
  background: white;
  border-color: var(--primary);
  color: var(--primary);
}

.step-label {
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--text-gray);
}
.wizard-step.active .step-label {
  color: var(--text-dark);
  font-weight: 600;
}

.category-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
}

.cat-card {
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.5rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.cat-card:hover {
  border-color: var(--primary);
  background: var(--primary-light);
}

.cat-card.selected {
  border-color: var(--primary);
  background: var(--primary-light);
  box-shadow: 0 0 0 2px var(--primary);
}

.cat-icon {
  font-size: 1.5rem;
  color: var(--primary);
  margin-bottom: 0.5rem;
}

.cat-card strong {
  font-size: 0.875rem;
  color: var(--text-dark);
}

.cat-card span {
  font-size: 0.75rem;
  color: var(--text-gray);
}

.wizard-footer {
  display: flex;
  justify-content: flex-end;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
}

/* ================= MODAL ================= */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(15, 23, 42, 0.5);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

.modal-overlay.active {
  display: flex;
}

.modal-content {
  background: white;
  border-radius: 16px;
  width: 100%;
  max-width: 500px;
  padding: 2rem;
  box-shadow: var(--shadow-lg);
  position: relative;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
}

.modal-title h2 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-dark);
}

.modal-title p {
  font-size: 0.875rem;
  color: var(--text-gray);
  margin-top: 0.25rem;
}

.btn-close {
  background: var(--bg-main);
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-gray);
  cursor: pointer;
}

.btn-close:hover {
  background: #e2e8f0;
  color: var(--text-dark);
}

.modal-body {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.modal-footer {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
}

.btn-secondary {
  background: white;
  border: 1px solid var(--border);
  color: var(--text-dark);
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
}

/* Toast */
#toast-container {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  z-index: 9999;
}

.vufix-toast {
  background: white;
  border-left: 4px solid var(--primary);
  box-shadow: var(--shadow-md);
  padding: 1rem;
  border-radius: 8px;
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  min-width: 300px;
}
.vufix-toast.success { border-color: var(--success); }
.vufix-toast.warning { border-color: var(--warning); }
.vufix-toast.danger { border-color: var(--danger); }

.toast-content strong {
  display: block;
  font-size: 0.875rem;
  color: var(--text-dark);
  margin-bottom: 0.25rem;
}
.toast-content p {
  font-size: 0.75rem;
  color: var(--text-gray);
}
"""

with open("style.css", "w") as f:
    f.write(css_content)

print("style.css written successfully.")
