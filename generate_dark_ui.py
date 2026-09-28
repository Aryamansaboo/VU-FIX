import os

css_content = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

:root {
  --bg-main: #09090b;
  --bg-card: #18181b;
  --bg-hover: #27272a;
  
  --primary: #0ea5e9;
  --primary-hover: #0284c7;
  --primary-glow: rgba(14, 165, 233, 0.4);
  
  --text-dark: #f4f4f5; /* Actually light text for dark mode */
  --text-gray: #a1a1aa;
  --border: #27272a;
  
  --success: #10b981;
  --success-bg: rgba(16, 185, 129, 0.1);
  --danger: #ef4444;
  --danger-bg: rgba(239, 68, 68, 0.1);
  --warning: #f59e0b;
  --warning-bg: rgba(245, 158, 11, 0.1);
  --info: #3b82f6;
  --info-bg: rgba(59, 130, 246, 0.1);
  
  --shadow-glow: 0 0 20px var(--primary-glow);
  --radius-lg: 16px;
  --radius-md: 12px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Outfit', sans-serif;
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
  background-image: radial-gradient(circle at top right, #1e1b4b, var(--bg-main) 40%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.auth-card {
  background: rgba(24, 24, 27, 0.7);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 480px;
  padding: 2.5rem;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

.auth-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 2rem;
  text-align: center;
}

.auth-logo {
  font-size: 2.5rem;
  background: -webkit-linear-gradient(45deg, #0ea5e9, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.5rem;
}

.auth-header h1 {
  font-size: 1.75rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.auth-header p {
  color: var(--text-gray);
  font-size: 0.875rem;
}

.auth-tabs {
  display: flex;
  background: #09090b;
  border-radius: var(--radius-md);
  padding: 0.25rem;
  margin-bottom: 1.5rem;
  border: 1px solid var(--border);
}

.auth-tab-btn {
  flex: 1;
  padding: 0.75rem;
  border: none;
  background: transparent;
  color: var(--text-gray);
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.auth-tab-btn.active {
  background: var(--bg-card);
  color: var(--text-dark);
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1.25rem;
}

.form-group label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-gray);
}

.form-control {
  background: #09090b;
  color: var(--text-dark);
  padding: 0.875rem 1rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 0.875rem;
  outline: none;
  transition: all 0.2s;
}

.form-control:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 2px var(--primary-glow);
}

.btn-primary {
  background: linear-gradient(135deg, #0ea5e9, #2563eb);
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  transition: all 0.3s;
  width: 100%;
  box-shadow: var(--shadow-glow);
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 0 25px rgba(14, 165, 233, 0.6);
}

.demo-presets {
  margin-top: 2.5rem;
  padding-top: 1.5rem;
  border-top: 1px dashed var(--border);
}

.preset-list {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.75rem;
}

.preset-btn {
  background: transparent;
  border: 1px solid var(--border);
  padding: 0.75rem 1rem;
  border-radius: 8px;
  text-align: left;
  display: flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  color: var(--text-dark);
}

.preset-btn:hover {
  background: var(--bg-hover);
  border-color: var(--text-gray);
}

.preset-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
}

/* ================= APP LAYOUT ================= */
.app-layout {
  display: flex;
  min-height: 100vh;
  padding: 1rem;
  gap: 1rem;
}

.sidebar {
  width: 280px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  display: flex;
  flex-direction: column;
  padding: 1.5rem;
}

.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 2rem;
}

.sidebar-brand h2 {
  font-size: 1.5rem;
  font-weight: 700;
  background: -webkit-linear-gradient(45deg, #0ea5e9, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.875rem 1rem;
  color: var(--text-gray);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 8px;
  transition: all 0.2s;
  margin-bottom: 0.5rem;
  cursor: pointer;
}

.nav-item:hover {
  background: rgba(255,255,255,0.05);
  color: var(--text-dark);
}

.nav-item.active {
  background: linear-gradient(135deg, rgba(14, 165, 233, 0.1), rgba(37, 99, 235, 0.1));
  color: var(--primary);
  border: 1px solid rgba(14, 165, 233, 0.2);
}

.main-content {
  flex: 1;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding: 2.5rem;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2.5rem;
}

.user-greeting {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.user-tags {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.user-tag {
  background: var(--bg-main);
  border: 1px solid var(--border);
  padding: 0.35rem 0.875rem;
  border-radius: 100px;
  font-size: 0.75rem;
  color: var(--text-gray);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: var(--bg-main);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.stat-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
}

.stat-info h3 {
  font-size: 0.75rem;
  color: var(--text-gray);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.stat-info p {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-dark);
}

.badge {
  padding: 0.25rem 0.75rem;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.badge.danger { background: var(--danger-bg); color: var(--danger); border: 1px solid rgba(239,68,68,0.2); }
.badge.info { background: var(--info-bg); color: var(--info); border: 1px solid rgba(59,130,246,0.2); }
.badge.warning { background: var(--warning-bg); color: var(--warning); border: 1px solid rgba(245,158,11,0.2); }
.badge.success { background: var(--success-bg); color: var(--success); border: 1px solid rgba(16,185,129,0.2); }

.complaints-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.complaint-card {
  background: var(--bg-main);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  transition: all 0.2s;
}

.complaint-card:hover {
  border-color: var(--primary);
  transform: translateY(-2px);
  box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5);
}

.complaint-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.complaint-id {
  font-size: 0.75rem;
  color: var(--primary);
  font-weight: 600;
  letter-spacing: 0.05em;
}

.complaint-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-top: 0.25rem;
}

.complaint-desc {
  font-size: 0.875rem;
  color: var(--text-gray);
  margin-bottom: 1.5rem;
  line-height: 1.5;
}

/* ================= WARDEN TABLE ================= */
.table-container {
  background: var(--bg-main);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.table-header-actions {
  padding: 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border);
  background: rgba(255,255,255,0.02);
}

.table-tabs {
  display: flex;
  gap: 0.5rem;
}

.table-tab {
  padding: 0.5rem 1.25rem;
  border: none;
  background: transparent;
  color: var(--text-gray);
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 100px;
  cursor: pointer;
  transition: all 0.2s;
}

.table-tab.active {
  background: var(--text-dark);
  color: var(--bg-main);
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 1.25rem;
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
  background: rgba(255,255,255,0.01);
}

.btn-manage {
  background: rgba(255,255,255,0.1);
  color: var(--text-dark);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-manage:hover {
  background: var(--primary);
  border-color: var(--primary);
}

/* ================= WIZARD ================= */
.wizard-container {
  background: var(--bg-main);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 2.5rem;
  max-width: 800px;
  margin: 0 auto;
}

.wizard-stepper {
  display: flex;
  justify-content: space-between;
  position: relative;
  margin-bottom: 3rem;
}
.wizard-stepper::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0; right: 0;
  height: 2px;
  background: var(--border);
  z-index: 1;
}

.wizard-step {
  position: relative;
  z-index: 2;
  background: var(--bg-main);
  padding: 0 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.step-circle {
  width: 40px; height: 40px;
  border-radius: 50%;
  background: var(--bg-card);
  border: 2px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: var(--text-gray);
}

.wizard-step.active .step-circle {
  border-color: var(--primary);
  background: var(--primary-glow);
  color: var(--primary);
  box-shadow: 0 0 15px var(--primary-glow);
}
.wizard-step.completed .step-circle {
  background: var(--primary);
  border-color: var(--primary);
  color: white;
}

.category-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1.25rem;
}

.cat-card {
  border: 1px solid var(--border);
  background: var(--bg-card);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
}

.cat-card:hover, .cat-card.selected {
  border-color: var(--primary);
  background: rgba(14, 165, 233, 0.05);
}

/* ================= MODAL ================= */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.8);
  backdrop-filter: blur(8px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-overlay.active { display: flex; }

.modal-content {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 520px;
  padding: 2.5rem;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,1);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 2rem;
}
.modal-title h2 { font-size: 1.5rem; }

.btn-secondary {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-dark);
  padding: 0.875rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
}
.btn-secondary:hover { background: var(--bg-hover); }

/* Hidden utility */
.hidden { display: none !important; }

/* Toast */
#toast-container { position: fixed; bottom: 2rem; right: 2rem; z-index: 9999; }
.vufix-toast { background: var(--bg-card); border-left: 4px solid var(--primary); padding: 1rem 1.5rem; border-radius: 8px; margin-top: 1rem; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5); display:flex; gap:1rem;}
"""

with open("style.css", "w") as f:
    f.write(css_content)

print("style.css written successfully.")
