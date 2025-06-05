import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';

import Navbar from './components/Navbar';
import Footer from './components/Footer';

import Home from './pages/Home';
import Profile from './pages/Profile';
import MyReviews from './pages/MyReviews';
import Login from './pages/Login';
import MovieDetail from './pages/MovieDetail';
import About from './pages/About';
import Terms from './pages/Terms';
import Privacy from './pages/Privacy';

function App() {
  return (
    <>
        <Navbar />
          <Routes>
            <Route path="/" element={<Navigate to="/home" replace />} />
            <Route path="/home" element={<Home />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/myreviews" element={<MyReviews />} />
            <Route path="/login" element={<Login />} />
            <Route path="/movie/:id" element={<MovieDetail />} />
            <Route path="/about" element={<About />} />
            <Route path="/terms" element={<Terms />} />
            <Route path="/privacy" element={<Privacy />} />
            <Route path="*" element={<div className="p-8 text-center">Page Not Found</div>} />
          </Routes>
        <Footer />
    </>
    
  );
}

export default App;
