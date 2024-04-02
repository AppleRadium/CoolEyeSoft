import axios from 'axios'
import React from 'react'

function Inventory(props) {
    const deleteFoodItem = (Item) => {
        axios.delete(`https://protected-dawn-61147-56a85301481c.herokuapp.com/fooditem/${Item}`)
            .then(res => console.log(res.data)) 
            .then(data => console.log(data))
    };
  
    return (
        <div>
            <div>
                <span style={{ fontWeight: 'bold, underline' }}>{props.fooditem.Item} : </span> {props.fooditem.Count}
                <button onClick={() => deleteFoodItem(props.fooditem.Item)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
            </div>
            <hr />
        </div>
    );
}
export default Inventory;