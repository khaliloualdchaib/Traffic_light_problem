import React from 'react';
import { MapContainer, TileLayer, Circle, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import './Map.css';

// Simulated traffic data
const trafficData = [
  { lat: 35.6895, lng: 139.6917, intensity: 0.8 }, // Tokyo center
  { lat: 35.6586, lng: 139.7454, intensity: 0.6 }, // Tokyo Tower
  { lat: 35.7101, lng: 139.8107, intensity: 0.7 }, // Asakusa
  { lat: 35.6890, lng: 139.7003, intensity: 0.4 }, // Shibuya
  { lat: 35.6896, lng: 139.7700, intensity: 0.5 }, // Tokyo Station
];

function Map() {
  return (
    <div className="map">
      <h2>Live Traffic Simulation</h2>
      <MapContainer center={[35.6895, 139.6917]} zoom={12} style={{ height: "500px", width: "100%" }}>
        {/* Base map layer */}
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />

        {/* Traffic simulation */}
        {trafficData.map((location, index) => (
          <Circle
            key={index}
            center={[location.lat, location.lng]}
            radius={location.intensity * 1000} // Simulate congestion intensity
            pathOptions={{ color: location.intensity > 0.6 ? 'red' : 'orange' }}
          >
            <Popup>
              <strong>Traffic Intensity:</strong> {Math.round(location.intensity * 100)}%
            </Popup>
          </Circle>
        ))}
      </MapContainer>
    </div>
  );
}

export default Map;
