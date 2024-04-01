import axios from 'axios'
import React from 'react'

function Inventory(props) {
    const deleteFoodItem = (foodItem) => {
    axios.delete(`https://protected-dawn-61147-56a85301481c.herokuapp.com/fooditem/${foodItem}`)
        .then(res => console.log(res.data)) 
        .then (data => console.log(data))}
  
    return (
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline' }}>{props.f} : </span> 
                <button onClick={() => deleteFoodItem(props.fooditem.foodItem)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default Inventory;