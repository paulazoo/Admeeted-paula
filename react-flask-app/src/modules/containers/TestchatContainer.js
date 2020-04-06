import React, { useEffect, Component } from 'react';
import Homepage from '../views/Homepage';
import { loadData } from "../actions";
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import Button from '@material-ui/core/Button';
import MainLayout from "../layouts/MainLayout";
import Testchat from "../views/Testchat";
import io from "socket.io-client";
import { TextField } from "@material-ui/core";

const socket = io("http://localhost:3000", {
    transports: ["polling","websocket"]
});


class TestchatContainer extends Component {
    constructor (props) {
      super(props)
      this.state = {
        msg: ""
      }
      this.handleChange = this.handleChange.bind(this)
      this.handleSubmit = this.handleSubmit.bind(this)
    }
    
    handleChange = event => {
        const {name, value} = event.target
        this.setState({ msg: value })
    };

    handleSubmit = event => {
        console.log(this.state.msg)
        socket.emit("sendmsg", this.state.msg)
        console.log("sent to socket?")
    };
     
    setSocketListeners () {
      socket.on('message', (data) => {
        console.log(data)
        socket.emit("sendmsg")
      })

      socket.on('connect', (data) => {
        console.log("socket connect!")
      })
    }
  
    componentDidMount () {
      this.setSocketListeners()
    }
  
    render () {
  
      return (
        <div className='TestchatContainer'>
            <TextField
                id="msg-textfield"
                multiline
                rowsMax="4"
                onChange={this.handleChange}
                variant="outlined"
                margin="dense"
            />
            <Button
                variant="contained"
                color="primary"
                onClick={this.handleSubmit}>
                Send
            </Button>
        </div> 
      )
    }
  }

export default withRouter(connect()(TestchatContainer))