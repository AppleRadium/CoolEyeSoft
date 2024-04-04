import axios from 'axios'
import React, {useState, useEffect} from 'react';

function TandH(){
    const [sensorData, setSensorData] = useState({ temperature: null, humidity: null });
    useEffect(() => {
        // Replace the URL with your actual backend endpoint
        axios.get('https://protected-dawn-61147-56a85301481c.herokuapp.com/sensor/latest')
          .then(response => {
            setSensorData(response.data);
          })
          .catch(error => console.error('There was an error!', error));
      }, []);

      if (!sensorData.temperature || !sensorData.humidity) {
        return <div>Loading...</div>;
      }
    
      return (
        <div>
          <p>Temperature: {sensorData.temperature}°F</p>
          <p>Humidity: {sensorData.humidity}%</p>
        </div>
      );
}export default TandH