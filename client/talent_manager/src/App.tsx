import './App.css';

import { Route, Routes } from "react-router-dom";

import Side from './components/side/index';

const App = () => {
  return (
    <Routes>
      <Route path="/side" element={<Side />} />
    </Routes>
  );
}

export default App;
