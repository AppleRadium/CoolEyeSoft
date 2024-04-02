import axios from 'axios'
import React from 'react'

function Inventory(props) {
    const deleteFoodItem = (itemId) => {
        // Notice that now we use `itemId` to construct the URL
        axios.delete(`https://protected-dawn-61147-56a85301481c.herokuapp.com/fooditem/${itemId}`)
            .then(res => console.log(res.data))
            .catch(error => console.error('Delete operation failed:', error));
    };

    return (
        <div>
            <div>
                <span style={{ fontWeight: 'bold, underline' }}>{props.fooditem.Item} : </span> {props.fooditem.Count}
                {/* Pass the `id` of the item to the deleteFoodItem function when the button is clicked */}
                <button onClick={() => deleteFoodItem(props.fooditem.id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px'}}>X</button>
            </div>
            <hr />
        </div>
    );
}

export default Inventory;