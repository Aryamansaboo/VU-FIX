import os

css_append = """
/* Missing dynamically injected classes by app.js */
.complaint-card-header {
  margin-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}
.complaint-meta-top {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  flex-wrap: wrap;
}
.ticket-id-tag {
  font-size: 0.75rem;
  color: var(--primary);
  font-weight: 600;
  letter-spacing: 0.05em;
  background: rgba(14, 165, 233, 0.1);
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
}
.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  background: rgba(255,255,255,0.1);
}
.status-badge.submitted { color: var(--text-gray); }
.status-badge.under_review { color: var(--warning); background: var(--warning-bg); }
.status-badge.assigned, .status-badge.in_progress { color: var(--info); background: var(--info-bg); }
.status-badge.resolved, .status-badge.closed { color: var(--success); background: var(--success-bg); }
.status-badge.escalated { color: var(--danger); background: var(--danger-bg); }

.priority-badge {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
}
.priority-badge.high, .priority-badge.critical { color: var(--danger); }
.priority-badge.medium { color: var(--warning); }
.priority-badge.low { color: var(--success); }

.complaint-title-block h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--text-dark);
}

.complaint-card-body {
  font-size: 0.875rem;
  color: var(--text-gray);
  margin-bottom: 1.25rem;
  line-height: 1.5;
}

.complaint-details-grid {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}
.complaint-detail-item, .tech-info-pill {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.875rem;
  color: var(--text-gray);
}
.tech-info-pill {
  color: var(--primary);
  background: var(--info-bg);
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  margin-top: 0.5rem;
}

.card-footer-actions {
  display: flex;
  gap: 0.75rem;
  margin-top: auto;
  border-top: 1px solid var(--border);
  padding-top: 1.25rem;
}
.btn-card-action {
  flex: 1;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-dark);
  padding: 0.5rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}
.btn-card-action:hover { background: var(--bg-hover); }
.btn-card-action.btn-open-escalate { border-color: rgba(239, 68, 68, 0.3); color: var(--danger); }
.btn-card-action.btn-open-escalate:hover { background: var(--danger-bg); }

.resolution-prompt-box {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
  border-radius: 8px;
  padding: 1rem;
  margin-top: 1rem;
}
.resolution-prompt-text {
  font-size: 0.875rem;
  color: var(--success);
  margin-bottom: 0.75rem;
  display: flex;
  gap: 0.5rem;
  align-items: center;
}
.resolve-confirm {
  background: var(--success);
  border-color: var(--success);
  color: white;
}
.resolve-confirm:hover { background: #059669; }

/* Timeline Node Classes */
.timeline-node {
  display: flex;
  gap: 1.5rem;
  position: relative;
}
.timeline-node::before {
  content: '';
  position: absolute;
  left: 20px;
  top: 40px;
  bottom: -1.5rem;
  width: 2px;
  background: var(--border);
}
.timeline-node:last-child::before { display: none; }
.timeline-node-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--bg-card);
  border: 2px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
  color: var(--text-gray);
}
.timeline-node.active .timeline-node-icon {
  border-color: var(--primary);
  background: var(--primary-glow);
  color: var(--primary);
}
.timeline-content-card {
  flex: 1;
  background: var(--bg-main);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.25rem;
}
.timeline-meta { display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 0.875rem; }
.timeline-body-text { font-size: 0.875rem; color: var(--text-gray); margin-bottom: 0.5rem; }
.timeline-author-tag { font-size: 0.75rem; color: var(--primary); }
"""

with open("style.css", "a") as f:
    f.write(css_append)

print("Appended dynamic classes to style.css")
