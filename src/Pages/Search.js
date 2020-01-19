import React, { Component } from 'react'
import './styles/Search.css'
import Results from '../Components/Results'
import YoutubeSearch from '../Components/YoutubeSearch'
class Search extends Component{
    
    constructor(props){
        super(props)

        this.state = {
            query:"Narendra Modi",
            isChips:[{name:"Adventure",isActive:false,id:1},
                     {name:"children",isActive:false,id:2},
                     {name:"comedy",isActive:false,id:3},
                     {name:"thriller",isActive:false,id:4},
                     {name:"romance",isActive:false,id:5},
                     {name:"action",isActive:false,id:6},
                     {name:"horror",isActive:false,id:7},
                     {name:"animation",isActive:false,id:8},
                     {name:"crime",isActive:false,id:9},
                     {name:"drama",isActive:false,id:10}
                    ]
            
        }

    //     name = forms.CharField(max_length=100, label='name')
    // adventure = forms.BooleanField(label='adventure', required=False)
    // children = forms.BooleanField(label='children', required=False)
    // comedy = forms.BooleanField(label='comedy', required=False)
    // thriller = forms.BooleanField(label='thriller', required=False)
    // romance = forms.BooleanField(label='romance', required=False)
    // action = forms.BooleanField(label='action', required=False)
    // horror = forms.BooleanField(label='horror', required=False)
    // animation = forms.BooleanField(label='animation', required=False)
    // crime = forms.BooleanField(label='crime', required=False)
    // drama = forms.BooleanField(label='drama', required=False)

    }

    searchquerys = (event)=>{
        console.log("CLicked ON Button to Reload")
        event.preventDefault();
        let name = event.target.query.value
        console.log("Name  - ",name)
        this.setState({
            query:name,
            isClicked:true
        })
        console.log(this.state)
    }
   
    render(){
        console.log("This is State's STate - ",this.state)
       if(this.state.isClicked === true){
           this.setState({
               isClicked:false
           })
           console.log("After Changing isClick from true to False")
       }

       return(
        <div className="page">
            <div className='mynav'>
                <div className='mynavTitle'>
                    my Title
                </div>
                <div className="mycontent">
                    <ul>
                        <li>Home</li>
                        <li>Search</li>
                        <li>Another</li>
                    </ul>
                </div>
            </div>
            <div className='mycontainer'>
                   <div id='b1'>
                       {/* blank1 */}
                   </div>
                   <form onSubmit={this.searchquerys} id='searchquery' style={{width:'100%',position:'absolute'}}>

                   <div id='search'>
                       <center><br /><br /><br />
                           <input name='query' id='searchinput' type='text' placeholder="Enter Movie Name" className='form-control' />
                       </center>
                   </div>

                   <div id='btn1'>
                    <center>
                    <button className='ripple' id='searchbtn'>Search Movies</button>
                    </center>
                    </div>

                   </form>
                   <div id='b2'>
                       {/* Blank2 */}
                       </div>
                    <div id='filters'>
                         {
                             this.state.isChips.map(mychipstate => 
                             <div onClick={(e)=>console.log(JSON.stringify(e))} value={mychipstate.id} className='chip'>
                             {mychipstate.name}
                         </div>)
                         }
                    </div>
                    <div id='results'>
                        <span class='lead container'>Youtube Recommendation </span>
                        <YoutubeSearch query={this.state.query} />
                    </div>
                   {/* <form>
                       <center>
                        <div className='sfgroup'>
                            <input type='text' placeholder='Enter Movies' />
                        </div>
                        <br />
                        <div className='sfgroup'>
                        <button type='submit'>
                                Search
                            </button>

                        <button type='button'>
                                Search
                            </button>
                        </div>
                        </center>
                    </form>

                    <form className='filters'>
                        <Row>
                            <Col>
                            Hello</Col>
                        </Row>
                   </form> */}
            </div>
        </div>
        )
    }
}

export default Search