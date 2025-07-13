import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
// import 병칭 from '파일명'
// import App from './App.jsx'
import App from './AppEx.jsx'

createRoot(document.getElementById('root')).render(
  <App />
)
