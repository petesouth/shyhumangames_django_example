import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Container } from 'react-bootstrap';
import EndlessScrollList from './components/EndlessScrollList';

function App() {
  return (
    <div>
      <EndlessScrollList />
    </div>
  );
}

export default App;
