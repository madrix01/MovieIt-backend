import React, { Component } from 'react';
import YoutubeSearch from './YoutubeSearch';
class Results extends Component {
    constructor(props){
        super(props)

        this.state = {

        }

        
    }
    render(){
        return(
            <div>
                Results Cards
                <YoutubeSearch query="Dora" />
            </div>
        );
    }
}
export default Results;