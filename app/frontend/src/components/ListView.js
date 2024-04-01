import Inventory from "./CoolEye"

export default function ListView(props) {
    console.log("Inventory data in ListView:", props.inventory); // Add this line
    return (
      <div>
        <ul>
          {props.inventory.map(fooditem => <Inventory key={fooditem.id} fooditem={fooditem}/>)}
        </ul>
      </div>
    );
  }
