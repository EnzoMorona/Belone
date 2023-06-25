import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';


import Loginpage from './routes/login.jsx';
import UserList from './routes/view.jsx';
import Cadastropage from './routes/cadastro.jsx';

import {createBrowserRouter, RouterProvider} from 'react-router-dom'

const router = createBrowserRouter([
  {
    element: <App />,
    children: [
      {
        path: '/',
        element: <Loginpage/>,
      },

      {
        path: '/view',
        element: <UserList/>,
      },
      
      {
        path: '/cadastro',
        element: <Cadastropage/>,
      }
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
)