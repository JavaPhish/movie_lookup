import React from "react";

import './App.css';
import MovieLookup  from "./search.js";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Movie Lookup</h1>
      </header>
      <body>
        <MovieLookup />
      </body>
    </div>
  );
}

export default App;
