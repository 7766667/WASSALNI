importScripts('https://www.gstatic.com/firebasejs/10.12.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.12.0/firebase-messaging-compat.js');

firebase.initializeApp({
  apiKey: "AIzaSyAihGwDfen5b1SjtPmzL0aToigleyGt6rM",
  authDomain: "wassalni-fa958.firebaseapp.com",
  projectId: "wassalni-fa958",
  storageBucket: "wassalni-fa958.firebasestorage.app",
  messagingSenderId: "63888443959",
  appId: "1:63888443959:web:3a28bf29c34c1f951d0db2"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
  const title = payload.notification.title;
  const options = { body: payload.notification.body, icon: '/icon.png' };
  self.registration.showNotification(title, options);
});
