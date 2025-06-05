import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white text-center py-4 text-sm mt-auto">
      <div>© {new Date().getFullYear()}</div>

      <div>
        <a
          href="https://sanjaygaire.github.io/"
          target="_blank"
          rel="noopener noreferrer"
          className="hover:text-green-400 transition-colors duration-200"
        >
          sanjaygaire
        </a>
      </div>

      <div className="space-x-4 mt-2">
        <Link to="/about" className="hover:text-green-400 transition-colors duration-200">
          About
        </Link>
        <Link to="/terms" className="hover:text-green-400 transition-colors duration-200">
          Terms
        </Link>
        <Link to="/privacy" className="hover:text-green-400 transition-colors duration-200">
          Privacy
        </Link>
      </div>
    </footer>
  );
};

export default Footer;
