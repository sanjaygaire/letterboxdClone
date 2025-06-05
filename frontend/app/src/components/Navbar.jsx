import { NavLink } from "react-router-dom"

function Navbar() {
  const linkClass =
    "hover:text-green-400 transition duration-200"

  const activeClass =
    "text-green-400 font-semibold"

  return (
    <header className="bg-gray-900 text-white px-6 py-4 flex justify-between items-center">
      <h1 className="text-2xl font-bold ">
        <NavLink to="/" className="hover:text-green-400 ">LetterboxD</NavLink>
      </h1>

      <nav className="flex flex-wrap gap-4 text-sm sm:text-base">
        <NavLink to="/home" className={({ isActive }) =>
            isActive ? `${linkClass} ${activeClass}` : linkClass
          }
        >
          Home
        </NavLink>
        <NavLink
          to="/login"
          className={({ isActive }) =>
            isActive ? `${linkClass} ${activeClass}` : linkClass
          }
        >
          Login
        </NavLink>
        <NavLink
          to="/profile"
          className={({ isActive }) =>
            isActive ? `${linkClass} ${activeClass}` : linkClass
          }
        >
          Profile
        </NavLink>
        <NavLink
          to="/myreviews"
          className={({ isActive }) =>
            isActive ? `${linkClass} ${activeClass}` : linkClass
          }
        >
          My Reviews
        </NavLink>
        <NavLink
          to="/log"
          className="bg-green-600 px-3 py-1 rounded hover:bg-green-500 text-white text-sm font-medium"
        >
          +Log
        </NavLink>
      </nav>
    </header>
  )
}

export default Navbar
