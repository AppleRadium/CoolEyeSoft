import Inventory from "./CoolEye"

export default function ListView(props){
    return(
        <div>
            <ul>
                {props.inventory.map(fooditem => <Inventory fooditem = {fooditem}/>)}
            </ul>
        </div>
    )
}
