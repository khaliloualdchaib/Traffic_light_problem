import './App.css';
import Header from './components/Header';
import Metrics from './components/Metrics';
import Map from './components/Map';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <Header />
      <div className="content">
        <Metrics />
        <Map />
      </div>
      <Footer />
    </div>
  );
}

export default App;
