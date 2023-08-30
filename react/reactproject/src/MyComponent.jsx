import Recat, {Component} from "react";

class MyComponent extends Component{
    render(){
        return(
            <div> 수정이의 첫번째 앨범은 {this.props.album}</div>
            
        )
    }
}

export default MyComponent;