import React from 'react';

function Movie() {
  return (
    <div className='bg-white text-black max-w-40 m-2 max-h-70 p-1 justify-between border-2 border-black hover:bg-green-600 hover:text-white'>
      <div className='w-full h-40 bg-gray-800 flex items-center justify-center overflow-hidden'>
        <img
          src="https://filmartgallery.com/cdn/shop/files/Inception-Vintage-Movie-Poster-Original.jpg?v=1738912645"
          className='w-full h-full object-cover'
          alt="movie poster"
        />
      </div>
      <div>
        <p className='font-semibold text-sm mt-1'>Inception</p>
        <div className='flex justify-between text-xs text-gray-700 mt-1'>
          <p>⭐ 4.5</p>
          <p>Watched ✅</p>
        </div>
      </div>
    </div>
  );
}

export default Movie;
