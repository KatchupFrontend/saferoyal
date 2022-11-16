// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {getAuth} from 'firebase/auth';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCc5JYw2Pnz-nUHK_4wTU5-apPV0DMBgeU",
  authDomain: "opionrooms.firebaseapp.com",
  projectId: "opionrooms",
  storageBucket: "opionrooms.appspot.com",
  messagingSenderId: "892252912063",
  appId: "1:892252912063:web:5850d707c39ce4cf7b490a"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export default app
