import React, { Component } from 'react';
import './styles/YoutubeSearch.css'
import { Row, Col } from 'react-bootstrap';

const YCards = (props)=>{
    console.log(props)


   return(<div className='card' style={{width:'100%'}}>
        <img src={props.props.snippet.thumbnails.high.url} class="card-img-top" alt="..."></img>
        <div className="card-body" style={{color:'black'}}>
    <h5 className="card-title"> {props.props.snippet.title} </h5>
    <p className="card-text"> {props.props.snippet.description} </p>
<a href={`https://youtube.com/watch?v=`+props.props.id.videoId} className="btn btn-primary">{props.props.id.kind == "youtube#channel"?'Visit Channel':'Play Video'}</a>
        
  </div>

    </div>)
}

class YoutubeSearch extends Component {
    constructor(props){
        super(props)

        this.state = {
            data:'',
            isyoutubeloaded:false,
            youtubevideos:[]
        }
        this.searchfor = props.query;
        fetch('https://www.googleapis.com/youtube/v3/search?key=AIzaSyCNEXvIF-9BdFHnpxUQ2iGbcShrJ_72BAA&part=snippet&q=Trailer '+this.searchfor,{
            method:"GET",
            headers:{
                'Content-type':'application/json'
            }
        }).then(results=>results.json().then(data=>{
            console.log(data.items)
             this.setState({
                youtubevideos:data,
                isyoutubeloaded:true
            })


            console.log(this.state.youtubevideos.items)
        })
        )

    }

    

    render(){
        const { isyoutubeloaded,youtubevideos } = this.state;
        console.log(youtubevideos.items)
        if(isyoutubeloaded === true){
            return(
                <div>
                   <center>
                   <Row className="container-fluid">
                       <center>Waiting for GOogle API's to Work !!</center>
                   {   

                        // youtubevideos.items.map(video => <Col key={video.etag}>
                        //     <YCards props={video} />
                        // </Col>)

                        }
                    </Row>
                   </center>
                </div>
            )
        }else{
            return(

                <div>
                    Results Cards
                    {this.state.data}
                </div>
            );
        }
        
    }
}
export default YoutubeSearch;