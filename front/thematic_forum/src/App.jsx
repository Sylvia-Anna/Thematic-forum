import { useState } from 'react'
import './App.css'
import Navbar from './components/Navbar.jsx';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import MainPage from '../src/pages/MainPage.jsx';
import SignInPage from './pages/SignInPage.jsx';
import SignUpPage from './pages/SignUpPage.jsx';
import NotFoundPage from './pages/NotFoundPage.jsx'

// Роуты для страниц
const router = createBrowserRouter([
  {
    path: '/',
    element: <MainPage/>,
    errorElement: <NotFoundPage />,
  },

  {
    path: '/signhup',
    element: <SignUpPage/>
  },

  {
    path:'/signin',
    element: <SignInPage />
  },
]);

function App() {
  return (
    <>
      <RouterProvider router={router} />
    </>
  )
}

export default App;
