/**
 * VUFIX — Hostel Maintenance & Complaint Management System
 * LocalStorage Persistent Reactive State Store (store.js)
 * Zero external dependencies. High performance reactive event bus.
 */

const STORAGE_KEY = 'vufix_app_state_v1';

// Default Initial Seed Data
const DEFAULT_PRESETS = {
  users: [
    {
      id: 'usr_aryaman',
      name: 'Aryaman Saboo',
      rollNo: 'ST20230042',
      email: 'aryaman.saboo@vijaybhoomi.edu.in',
      hostel: 'Hostel A',
      block: 'Block B3',
      room: 'B3-304',
      hostelRoomDisplay: 'Hostel A, Block B3, Room B3-304',
      avatar: 'AS',
      role: 'student',
      password: 'password123'
    },
    {
      id: 'usr_parth',
      name: 'Parth Pawar',
      rollNo: 'ST20230088',
      email: 'parth.pawar@vijaybhoomi.edu.in',
      hostel: 'Hostel A',
      block: 'Block A1',
      room: 'A1-101',
      hostelRoomDisplay: 'Hostel A, Block A1, Room A1-101',
      avatar: 'PP',
      role: 'student',
      password: 'password123'
    },
    {
      id: 'usr_rinu',
      name: 'Rinu Babu',
      title: 'Hostel Warden',
      adminId: 'ADM-WARDEN-01',
      email: 'rinu.babu@vijaybhoomi.edu.in',
      avatar: 'RB',
      role: 'warden',
      password: 'admin123'
    }
  ],
  technicians: [
    {
      id: 'tech_1',
      name: 'Ramesh Kumar',
      specialty: 'Electrical Specialist',
      phone: '+91 98123 45678',
      avatar: 'RK',
      rating: 4.8,
      status: 'Available',
      icon: 'fa-bolt',
      color: '#f59e0b'
    },
    {
      id: 'tech_2',
      name: 'Suresh Sharma',
      specialty: 'Plumbing Specialist',
      phone: '+91 98234 56789',
      avatar: 'SS',
      rating: 4.7,
      status: 'On Duty',
      icon: 'fa-faucet-drip',
      color: '#0ea5e9'
    },
    {
      id: 'tech_3',
      name: 'Vikas Patil',
      specialty: 'IT & Network Specialist',
      phone: '+91 98345 67890',
      avatar: 'VP',
      rating: 4.9,
      status: 'Busy',
      icon: 'fa-wifi',
      color: '#8b5cf6'
    },
    {
      id: 'tech_4',
      name: 'Sunita Devi',
      specialty: 'Housekeeping Specialist',
      phone: '+91 98456 78901',
      avatar: 'SD',
      rating: 4.8,
      status: 'Available',
      icon: 'fa-broom',
      color: '#10b981'
    }
  ],
  complaints: [
    {
      id: 'TKT-2026-0842',
      studentId: 'usr_aryaman',
      studentName: 'Aryaman Saboo',
      rollNo: 'ST20230042',
      email: 'aryaman.saboo@vijaybhoomi.edu.in',
      room: 'Hostel A, Block B3, Room B3-304',
      category: 'Electrical',
      subcategory: 'Fan / Regulator',
      title: 'Ceiling Fan Making Loud Scraping Noise & Wobbling',
      description: 'The ceiling fan in Room B3-304 started making a harsh metallic grinding sound when switched past speed 2. It wobbles unsteadily and poses a safety concern during sleep.',
      priority: 'High',
      preferredSlot: 'Morning (9:00 AM - 12:00 PM)',
      status: 'In Progress',
      createdAt: '2026-09-19T14:30:00.000Z',
      eta: '2026-09-21T16:00:00.000Z',
      assignedTechnicianId: 'tech_1',
      assignedTechnicianName: 'Ramesh Kumar',
      assignedTechnicianPhone: '+91 98123 45678',
      assignedTechnicianAvatar: 'RK',
      assignedTechnicianSpecialty: 'Electrical Specialist',
      escalated: false,
      escalationReason: null,
      studentConfirmed: null,
      images: [
        'https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=500&auto=format&fit=crop&q=60'
      ],
      timeline: [
        {
          id: 'log_1',
          timestamp: '2026-09-19T14:30:00.000Z',
          title: 'Complaint Submitted',
          text: 'Ticket TKT-2026-0842 successfully created by Aryaman Saboo via VUFIX Portal.',
          author: 'Aryaman Saboo',
          badge: 'Submitted',
          type: 'submitted'
        },
        {
          id: 'log_2',
          timestamp: '2026-09-19T15:15:00.000Z',
          title: 'Under Review by Warden',
          text: 'Reviewed complaint details. Classified as High priority due to safety risk.',
          author: 'Rinu Babu (Warden)',
          badge: 'Under Review',
          type: 'review'
        },
        {
          id: 'log_3',
          timestamp: '2026-09-20T09:30:00.000Z',
          title: 'Technician Assigned',
          text: 'Assigned Ramesh Kumar (Electrical Specialist) to inspect motor bearings and regulator unit.',
          author: 'Rinu Babu (Warden)',
          badge: 'Assigned',
          type: 'assigned'
        },
        {
          id: 'log_4',
          timestamp: '2026-09-20T11:00:00.000Z',
          title: 'Work In Progress & Parts Sourced',
          text: 'Technician inspected fan assembly. Replacing worn capacitor and tightening mounting bracket. Expected completion by 4:00 PM today.',
          author: 'Ramesh Kumar (Technician)',
          badge: 'In Progress',
          type: 'in_progress'
        }
      ]
    },
    {
      id: 'TKT-2026-0791',
      studentId: 'usr_aryaman',
      studentName: 'Aryaman Saboo',
      rollNo: 'ST20230042',
      email: 'aryaman.saboo@vijaybhoomi.edu.in',
      room: 'Hostel A, Block B3, Room B3-304',
      category: 'Plumbing',
      subcategory: 'Washbasin / Drainage',
      title: 'Bathroom Washbasin Water Drainage Clogged',
      description: 'Water drains extremely slowly in the washbasin causing stagnant water backup during morning use.',
      priority: 'Medium',
      preferredSlot: 'Afternoon (12:00 PM - 4:00 PM)',
      status: 'Resolved',
      createdAt: '2026-09-17T09:15:00.000Z',
      resolvedAt: '2026-09-18T11:30:00.000Z',
      eta: '2026-09-18T12:00:00.000Z',
      assignedTechnicianId: 'tech_2',
      assignedTechnicianName: 'Suresh Sharma',
      assignedTechnicianPhone: '+91 98234 56789',
      assignedTechnicianAvatar: 'SS',
      assignedTechnicianSpecialty: 'Plumbing Specialist',
      escalated: false,
      escalationReason: null,
      studentConfirmed: null, // Pending confirmation by student!
      images: [
        'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=500&auto=format&fit=crop&q=60'
      ],
      timeline: [
        {
          id: 'log_201',
          timestamp: '2026-09-17T09:15:00.000Z',
          title: 'Complaint Submitted',
          text: 'Ticket created by Aryaman Saboo.',
          author: 'Aryaman Saboo',
          badge: 'Submitted',
          type: 'submitted'
        },
        {
          id: 'log_202',
          timestamp: '2026-09-17T10:00:00.000Z',
          title: 'Technician Assigned',
          text: 'Assigned Suresh Sharma (Plumbing Specialist).',
          author: 'Rinu Babu (Warden)',
          badge: 'Assigned',
          type: 'assigned'
        },
        {
          id: 'log_203',
          timestamp: '2026-09-18T11:30:00.000Z',
          title: 'Work Completed & Marked Resolved',
          text: 'Cleared blockage from washbasin P-trap. Water flow tested & fully restored.',
          author: 'Suresh Sharma (Technician)',
          badge: 'Resolved',
          type: 'resolved'
        }
      ]
    },
    {
      id: 'TKT-2026-0810',
      studentId: 'usr_parth',
      studentName: 'Parth Pawar',
      rollNo: 'ST20230088',
      email: 'parth.pawar@vijaybhoomi.edu.in',
      room: 'Hostel A, Block A1, Room A1-101',
      category: 'IT / Network',
      subcategory: 'Wi-Fi Router / LAN',
      title: 'Block A1 Wi-Fi Router Intermittent Connection Drop',
      description: 'The Wi-Fi access point in corridor A1 disconnects every 5 minutes. Cannot attend live online lectures or submit online assignments.',
      priority: 'Critical',
      preferredSlot: 'Any Time',
      status: 'Escalated',
      createdAt: '2026-09-18T16:00:00.000Z',
      escalatedAt: '2026-09-20T10:15:00.000Z',
      eta: '2026-09-19T18:00:00.000Z',
      assignedTechnicianId: 'tech_3',
      assignedTechnicianName: 'Vikas Patil',
      assignedTechnicianPhone: '+91 98345 67890',
      assignedTechnicianAvatar: 'VP',
      assignedTechnicianSpecialty: 'IT & Network Specialist',
      escalated: true,
      escalationReason: 'No technician visited despite 24-hour ETA passed. Unable to study for upcoming midterm exams.',
      studentConfirmed: null,
      images: [
        'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=500&auto=format&fit=crop&q=60'
      ],
      timeline: [
        {
          id: 'log_301',
          timestamp: '2026-09-18T16:00:00.000Z',
          title: 'Complaint Submitted',
          text: 'Submitted by Parth Pawar.',
          author: 'Parth Pawar',
          badge: 'Submitted',
          type: 'submitted'
        },
        {
          id: 'log_302',
          timestamp: '2026-09-19T09:00:00.000Z',
          title: 'Technician Assigned',
          text: 'Vikas Patil assigned for router diagnostics.',
          author: 'Rinu Babu (Warden)',
          badge: 'Assigned',
          type: 'assigned'
        },
        {
          id: 'log_303',
          timestamp: '2026-09-20T10:15:00.000Z',
          title: '🚨 Escalated to Warden',
          text: 'Escalated by student: "No technician visited despite 24-hour ETA passed. Urgent exam prep affected."',
          author: 'Parth Pawar (Student)',
          badge: '🚨 Escalated',
          type: 'escalated'
        }
      ]
    },
    {
      id: 'TKT-2026-0650',
      studentId: 'usr_aryaman',
      studentName: 'Aryaman Saboo',
      rollNo: 'ST20230042',
      email: 'aryaman.saboo@vijaybhoomi.edu.in',
      room: 'Hostel A, Block B3, Room B3-304',
      category: 'Electrical',
      subcategory: 'Switchboard / Socket',
      title: 'Study Desk Socket Internal Wiring Loose',
      description: 'Right wall power socket sparking occasionally when laptop charger plugged in.',
      priority: 'Low',
      preferredSlot: 'Evening (4:00 PM - 8:00 PM)',
      status: 'Closed',
      createdAt: '2026-09-10T11:00:00.000Z',
      resolvedAt: '2026-09-11T15:20:00.000Z',
      closedAt: '2026-09-11T16:00:00.000Z',
      eta: '2026-09-11T18:00:00.000Z',
      assignedTechnicianId: 'tech_1',
      assignedTechnicianName: 'Ramesh Kumar',
      assignedTechnicianPhone: '+91 98123 45678',
      assignedTechnicianAvatar: 'RK',
      assignedTechnicianSpecialty: 'Electrical Specialist',
      escalated: false,
      escalationReason: null,
      studentConfirmed: true,
      rating: 5,
      ratingComment: 'Quick response! Ramesh fixed the socket terminal wiring securely within 15 minutes.',
      images: [],
      timeline: [
        {
          id: 'log_401',
          timestamp: '2026-09-10T11:00:00.000Z',
          title: 'Complaint Submitted',
          text: 'Ticket created by Aryaman Saboo.',
          author: 'Aryaman Saboo',
          badge: 'Submitted',
          type: 'submitted'
        },
        {
          id: 'log_402',
          timestamp: '2026-09-11T14:00:00.000Z',
          title: 'Technician Assigned & Fixed',
          text: 'Socket replaced with modular safety switchboard by Ramesh Kumar.',
          author: 'Ramesh Kumar',
          badge: 'Resolved',
          type: 'resolved'
        },
        {
          id: 'log_403',
          timestamp: '2026-09-11T16:00:00.000Z',
          title: 'Verified & Closed by Student',
          text: 'Aryaman Saboo confirmed issue resolved with 5-star rating.',
          author: 'Aryaman Saboo',
          badge: 'Closed',
          type: 'closed'
        }
      ]
    },
    {
      id: 'TKT-2026-0855',
      studentId: 'usr_parth',
      studentName: 'Parth Pawar',
      rollNo: 'ST20230088',
      email: 'parth.pawar@vijaybhoomi.edu.in',
      room: 'Hostel A, Block A1, Room A1-101',
      category: 'Carpentry / Furniture',
      subcategory: 'Door Lock / Latch',
      title: 'Main Room Door Lock Cylinder Jammed',
      description: 'The key gets stuck inside the brass lock cylinder when trying to lock from outside.',
      priority: 'High',
      preferredSlot: 'Morning (9:00 AM - 12:00 PM)',
      status: 'Submitted',
      createdAt: '2026-09-20T18:45:00.000Z',
      eta: null,
      assignedTechnicianId: null,
      escalated: false,
      escalationReason: null,
      studentConfirmed: null,
      images: [],
      timeline: [
        {
          id: 'log_501',
          timestamp: '2026-09-20T18:45:00.000Z',
          title: 'Complaint Submitted',
          text: 'Ticket created by Parth Pawar.',
          author: 'Parth Pawar',
          badge: 'Submitted',
          type: 'submitted'
        }
      ]
    }
  ],
  notifications: [
    {
      id: 'notif_1',
      title: 'Technician Update',
      message: 'Ramesh Kumar posted an update on TKT-2026-0842 (Electrical): "Replacing capacitor..."',
      timestamp: '2026-09-20T11:00:00.000Z',
      read: false,
      type: 'info'
    },
    {
      id: 'notif_2',
      title: '🚨 Urgent Escalation Alert',
      message: 'Parth Pawar escalated TKT-2026-0810 (IT / Network Router Drop). Action required!',
      timestamp: '2026-09-20T10:15:00.000Z',
      read: false,
      type: 'warning'
    },
    {
      id: 'notif_3',
      title: 'Issue Marked Resolved',
      message: 'Suresh Sharma marked washbasin complaint TKT-2026-0791 as Resolved. Please confirm repair.',
      timestamp: '2026-09-18T11:30:00.000Z',
      read: true,
      type: 'success'
    }
  ]
};

class Store {
  constructor() {
    this.listeners = [];
    this.state = this.loadState();
  }

  loadState() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        // Ensure default users and technicians exist if storage is partial
        if (!parsed.currentUser) {
          parsed.currentUser = parsed.users[0]; // Default Aryaman Saboo
        }
        return parsed;
      }
    } catch (e) {
      console.warn('Failed to load VUFIX state from localStorage:', e);
    }
    // Return cloned default seed state
    const initialState = JSON.parse(JSON.stringify(DEFAULT_PRESETS));
    initialState.currentUser = initialState.users[0]; // Aryaman Saboo
    this.saveState(initialState);
    return initialState;
  }

  saveState(stateToSave = this.state) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(stateToSave));
    } catch (e) {
      console.error('Failed to persist VUFIX state to localStorage:', e);
    }
  }

  subscribe(listener) {
    this.listeners.push(listener);
    return () => {
      this.listeners = this.listeners.filter(l => l !== listener);
    };
  }

  notify() {
    this.saveState();
    this.listeners.forEach(listener => listener(this.state));
  }

  // --- User & Auth API ---
  get currentUser() {
    return this.state.currentUser;
  }

  get users() {
    return this.state.users;
  }

  get technicians() {
    return this.state.technicians;
  }

  get complaints() {
    return this.state.complaints;
  }

  get notifications() {
    return this.state.notifications;
  }

  login(emailOrRoll, password) {
    const query = emailOrRoll.trim().toLowerCase();
    const user = this.state.users.find(
      u => u.email.toLowerCase() === query || (u.rollNo && u.rollNo.toLowerCase() === query) || (u.adminId && u.adminId.toLowerCase() === query)
    );

    if (!user) {
      throw new Error('User account not found. Please check your Email / Roll No.');
    }
    
    // Simple password check fallback for demo
    if (password && user.password && user.password !== password) {
      // For demo smoothness, accept password if entered or match
    }

    this.state.currentUser = user;
    this.addNotification({
      title: 'Logged In Successfully',
      message: `Welcome back, ${user.name}!`,
      type: 'info'
    });
    this.notify();
    return user;
  }

  quickFillUser(userId) {
    const user = this.state.users.find(u => u.id === userId);
    if (user) {
      this.state.currentUser = user;
      this.notify();
    }
    return user;
  }

  registerUser(userData) {
    const existing = this.state.users.find(u => u.email.toLowerCase() === userData.email.toLowerCase());
    if (existing) {
      throw new Error('An account with this email address already exists.');
    }

    const nameParts = userData.name.trim().split(' ');
    const avatar = nameParts.length >= 2 
      ? (nameParts[0][0] + nameParts[1][0]).toUpperCase()
      : userData.name.substring(0, 2).toUpperCase();

    const newUser = {
      id: 'usr_' + Date.now(),
      name: userData.name,
      rollNo: userData.rollNo || 'ST' + Math.floor(100000 + Math.random() * 900000),
      email: userData.email,
      hostel: userData.hostel || 'Hostel A',
      block: userData.block || 'Block B3',
      room: userData.room || 'B3-304',
      hostelRoomDisplay: `${userData.hostel || 'Hostel A'}, ${userData.block || 'Block B3'}, Room ${userData.room || 'B3-304'}`,
      avatar: avatar,
      role: 'student',
      password: userData.password || 'password123'
    };

    this.state.users.push(newUser);
    this.state.currentUser = newUser;
    this.addNotification({
      title: 'Registration Successful',
      message: `Welcome to VUFIX, ${newUser.name}! Your account has been registered.`,
      type: 'success'
    });
    this.notify();
    return newUser;
  }

  logout() {
    this.state.currentUser = null;
    this.notify();
  }

  // --- Complaints API ---
  createComplaint(data) {
    const user = this.currentUser;
    if (!user || user.role !== 'student') {
      throw new Error('Only logged-in students can submit maintenance complaints.');
    }

    const ticketId = 'TKT-2026-' + String(Math.floor(1000 + Math.random() * 9000));
    const nowIso = new Date().toISOString();

    const newComplaint = {
      id: ticketId,
      studentId: user.id,
      studentName: user.name,
      rollNo: user.rollNo,
      email: user.email,
      room: user.hostelRoomDisplay || `${user.hostel}, ${user.block}, Room ${user.room}`,
      category: data.category,
      subcategory: data.subcategory || 'General Issue',
      title: data.title,
      description: data.description,
      priority: data.priority || 'Medium',
      preferredSlot: data.preferredSlot || 'Any Time',
      status: 'Submitted',
      createdAt: nowIso,
      eta: null,
      assignedTechnicianId: null,
      assignedTechnicianName: null,
      escalated: false,
      escalationReason: null,
      studentConfirmed: null,
      images: data.images || [],
      timeline: [
        {
          id: 'log_' + Date.now(),
          timestamp: nowIso,
          title: 'Complaint Submitted',
          text: `Ticket ${ticketId} registered under category [${data.category}]. Preferred visit slot: ${data.preferredSlot}.`,
          author: user.name,
          badge: 'Submitted',
          type: 'submitted'
        }
      ]
    };

    this.state.complaints.unshift(newComplaint);
    this.addNotification({
      title: 'Complaint Filed Successfully',
      message: `Ticket #${ticketId} created. Hostel maintenance team has been notified.`,
      type: 'success'
    });
    this.notify();
    return newComplaint;
  }

  updateComplaintWarden(ticketId, updates) {
    const complaint = this.state.complaints.find(c => c.id === ticketId);
    if (!complaint) throw new Error('Complaint ticket not found');

    const nowIso = new Date().toISOString();
    const warden = this.currentUser;
    const authorName = warden ? (warden.name + ' (Warden)') : 'Hostel Administration';

    if (updates.status && updates.status !== complaint.status) {
      const oldStatus = complaint.status;
      complaint.status = updates.status;

      let logTitle = `Status Updated to [${updates.status}]`;
      let logType = 'info';

      if (updates.status === 'Under Review') {
        logTitle = 'Under Review by Warden';
        logType = 'review';
      } else if (updates.status === 'Assigned') {
        logTitle = 'Technician Assigned';
        logType = 'assigned';
      } else if (updates.status === 'In Progress') {
        logTitle = 'Work In Progress';
        logType = 'in_progress';
      } else if (updates.status === 'On Hold') {
        logTitle = 'Put On Hold';
        logType = 'warning';
      } else if (updates.status === 'Resolved') {
        logTitle = 'Issue Marked Resolved';
        logType = 'resolved';
        complaint.resolvedAt = nowIso;
        complaint.studentConfirmed = null; // Awaiting student confirmation!
      } else if (updates.status === 'Closed') {
        logTitle = 'Ticket Closed';
        logType = 'closed';
        complaint.closedAt = nowIso;
      }

      complaint.timeline.push({
        id: 'log_' + Date.now(),
        timestamp: nowIso,
        title: logTitle,
        text: `Status changed from ${oldStatus} to ${updates.status}.` + (updates.note ? ` Note: ${updates.note}` : ''),
        author: authorName,
        badge: updates.status,
        type: logType
      });
    }

    if (updates.technicianId !== undefined) {
      const tech = this.state.technicians.find(t => t.id === updates.technicianId);
      if (tech) {
        complaint.assignedTechnicianId = tech.id;
        complaint.assignedTechnicianName = tech.name;
        complaint.assignedTechnicianPhone = tech.phone;
        complaint.assignedTechnicianAvatar = tech.avatar;
        complaint.assignedTechnicianSpecialty = tech.specialty;

        if (complaint.status === 'Submitted' || complaint.status === 'Under Review') {
          complaint.status = 'Assigned';
        }

        complaint.timeline.push({
          id: 'log_tech_' + Date.now(),
          timestamp: nowIso,
          title: `Assigned Technician: ${tech.name}`,
          text: `Assigned specialist ${tech.name} (${tech.specialty}, Contact: ${tech.phone}).`,
          author: authorName,
          badge: 'Assigned',
          type: 'assigned'
        });
      }
    }

    if (updates.eta !== undefined) {
      complaint.eta = updates.eta;
      complaint.timeline.push({
        id: 'log_eta_' + Date.now(),
        timestamp: nowIso,
        title: 'Estimated Resolution Time (ETA) Set',
        text: `Target completion set for ${new Date(updates.eta).toLocaleString('en-IN', { dateStyle: 'medium', timeStyle: 'short' })}.`,
        author: authorName,
        badge: 'ETA Update',
        type: 'eta'
      });
    }

    if (updates.note && !updates.status) {
      complaint.timeline.push({
        id: 'log_note_' + Date.now(),
        timestamp: nowIso,
        title: 'Maintenance Progress Note',
        text: updates.note,
        author: authorName,
        badge: 'Update Note',
        type: 'note'
      });
    }

    this.addNotification({
      title: `Ticket #${complaint.id} Updated`,
      message: `Status updated to ${complaint.status}. ${complaint.assignedTechnicianName ? 'Assigned: ' + complaint.assignedTechnicianName : ''}`,
      type: 'info'
    });

    this.notify();
    return complaint;
  }

  escalateComplaint(ticketId, reason) {
    const complaint = this.state.complaints.find(c => c.id === ticketId);
    if (!complaint) throw new Error('Complaint ticket not found');

    const nowIso = new Date().toISOString();
    const user = this.currentUser;

    complaint.escalated = true;
    complaint.escalatedAt = nowIso;
    complaint.escalationReason = reason;
    complaint.status = 'Escalated';

    complaint.timeline.push({
      id: 'log_esc_' + Date.now(),
      timestamp: nowIso,
      title: '🚨 Escalated to Hostel Warden',
      text: `Student ${user ? user.name : 'Resident'} escalated this complaint: "${reason}".`,
      author: user ? `${user.name} (Student)` : 'Resident',
      badge: '🚨 Escalated',
      type: 'escalated'
    });

    this.addNotification({
      title: '🚨 Ticket Escalated to Warden',
      message: `High visibility alert sent to Warden Rinu Babu for Ticket #${complaint.id}.`,
      type: 'warning'
    });

    this.notify();
    return complaint;
  }

  confirmResolution(ticketId, isFixed, feedback = {}) {
    const complaint = this.state.complaints.find(c => c.id === ticketId);
    if (!complaint) throw new Error('Complaint ticket not found');

    const nowIso = new Date().toISOString();
    const user = this.currentUser;

    if (isFixed) {
      complaint.status = 'Closed';
      complaint.studentConfirmed = true;
      complaint.closedAt = nowIso;
      if (feedback.rating) complaint.rating = feedback.rating;
      if (feedback.comment) complaint.ratingComment = feedback.comment;

      complaint.timeline.push({
        id: 'log_conf_' + Date.now(),
        timestamp: nowIso,
        title: 'Verified & Confirmed Fixed by Resident',
        text: `Student confirmed repair completion. ${feedback.rating ? 'Rating: ' + '⭐'.repeat(feedback.rating) : ''} ${feedback.comment ? '"' + feedback.comment + '"' : ''}`,
        author: user ? user.name : 'Student',
        badge: 'Closed',
        type: 'closed'
      });

      this.addNotification({
        title: 'Issue Closed & Verified',
        message: `Thank you for confirming resolution of #${complaint.id}!`,
        type: 'success'
      });
    } else {
      complaint.status = 'In Progress';
      complaint.studentConfirmed = false;
      complaint.escalated = true; // Flag for attention since fix failed

      complaint.timeline.push({
        id: 'log_reopen_' + Date.now(),
        timestamp: nowIso,
        title: '🔴 Reopened by Resident (Issue Still Broken)',
        text: `Student reported repair was incomplete or ineffective: "${feedback.comment || 'Issue persists after technician visit.'}". Reopened & escalated for follow-up.`,
        author: user ? user.name : 'Student',
        badge: 'Reopened',
        type: 'escalated'
      });

      this.addNotification({
        title: 'Ticket Reopened',
        message: `Warden has been alerted that #${complaint.id} remains unresolved.`,
        type: 'warning'
      });
    }

    this.notify();
    return complaint;
  }

  addNotification(notif) {
    this.state.notifications.unshift({
      id: 'notif_' + Date.now(),
      title: notif.title,
      message: notif.message,
      timestamp: new Date().toISOString(),
      read: false,
      type: notif.type || 'info'
    });
    // Keep max 20 notifications
    if (this.state.notifications.length > 20) {
      this.state.notifications.pop();
    }
  }

  markNotificationsRead() {
    this.state.notifications.forEach(n => n.read = true);
    this.notify();
  }

  resetToDefaultData() {
    const initialState = JSON.parse(JSON.stringify(DEFAULT_PRESETS));
    initialState.currentUser = initialState.users[0];
    this.state = initialState;
    this.saveState();
    this.notify();
  }

  // --- Statistics helper ---
  getStats() {
    const user = this.currentUser;
    const isWarden = user && user.role === 'warden';

    let userComplaints = this.state.complaints;
    if (!isWarden && user) {
      userComplaints = this.state.complaints.filter(c => c.studentId === user.id);
    }

    const total = userComplaints.length;
    const pending = userComplaints.filter(c => c.status === 'Submitted' || c.status === 'Under Review').length;
    const inProgress = userComplaints.filter(c => c.status === 'Assigned' || c.status === 'In Progress').length;
    const escalated = userComplaints.filter(c => c.escalated || c.status === 'Escalated').length;
    const resolved = userComplaints.filter(c => c.status === 'Resolved' || c.status === 'Closed').length;

    return {
      total,
      pending,
      inProgress,
      escalated,
      resolved
    };
  }
}

// Export global singleton instance
window.VUFIXStore = new Store();
