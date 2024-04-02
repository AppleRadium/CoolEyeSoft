import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'
import ListView from "./components/ListView"

function App() {
  const [inventory, setInventory] = useState([{}])
  const [Item, setFoodItem] = useState('')
  const [Count, setCount] = useState('')

  //read all items
  useEffect(() => {
    axios.get('https://protected-dawn-61147-56a85301481c.herokuapp.com/fooditem/')
      .then(res => {
        console.log("Received data:", res.data); // Logs fetched data
        const transformedItems = inventory.map(item => ({
          ...item,
          id: item._id.$oid // or just item._id if it's already in the right format
        }));
        setInventory(transformedItems); // Update this line if the data structure is as shown
        console.log("Inventory state after set:", inventory); // Might log the old state due to async state update
      })
      .catch(error => console.error('Fetching inventory error:', error));
}, []);

useEffect(() => {
  console.log("Updated inventory state:", inventory);
}, [inventory]);

  //Post an item
  const addFoodItem = () => {
  
  axios.post('https://protected-dawn-61147-56a85301481c.herokuapp.com/fooditem/', {"Item": Item, "Count": Count})
    .then(res => console.log(res))
    .catch(err => console.log(err));
};
  return (
    <div className="App">
       <div className = "App list-group-item justify-content-center align-items-center mx-auto"style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}}></div>
      <h1 className = "card text-white bg-primary mb-1" >
        CoolEye</h1>
      <div className = "card-body"> 
      <h5 className = "card text-white bg-dark mb-3"> Live Feed</h5>
      <span>
        <input className = "mb-2 form-control titleIn" onChange ={event =>setFoodItem(event.target.value)} placeholder='Name of Food Item'/>
        <input className = "mb-2 form-control titleIn" onChange ={event =>setCount(event.target.value)} placeholder='Item Count'/>
         <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"fontWeight":"bold"}} onClick={addFoodItem}>Add Food Item</button>
      </span>
      <h5 className = "card text-white bg-dark mb-3"> Inventory</h5>
      <div>
        <ListView inventory ={inventory}/>
      </div>
      </div>
    </div>
  );
}

export default App;
