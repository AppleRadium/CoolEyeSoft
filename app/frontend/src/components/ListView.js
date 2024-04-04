import Inventory from "./CoolEye"

export default function ListView(props) {
    console.log("Inventory data in ListView:", props.inventory); 
    return (
      <div>
        {props.inventory && props.inventory.length > 0 ? (
          <ul>
            {props.inventory.map((fooditem, index) => (
              <Inventory key={index} fooditem={fooditem} />
            ))}
          </ul>
        ) : (
          <p>No items to display.</p>
        )}
      </div>
    );
}


