import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import {BrowserRouter} from 'react-router-dom' // React 에서  Router기능을 사용할수있게끔 허용

createRoot(document.getElementById('root')).render(
  // App이라는 컴포넌트에서 Router기능을 사용할수있게끔 허용함. <- <BrowserRouter><App/></BrowserRouter>
<BrowserRouter>
  <App/>
</BrowserRouter>
  

)
