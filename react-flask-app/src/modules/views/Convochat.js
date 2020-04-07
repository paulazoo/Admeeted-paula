import React, {useState, useEffect, Component } from "react";
import Icon from '@material-ui/core/Icon';
import MainLayout from "../layouts/MainLayout";
import {
    Select,
    TextField,
    MenuItem,
    Card,
    CardHeader,
    CardContent,
    CardActions,
    Divider,
    InputLabel,
    FormControl,
    Typography,
    Button,
    IconButton,
    Chip,
    Grid
} from "@material-ui/core";
import { withStyles } from '@material-ui/core/styles';
import ReactJson from "react-json-view";
import Loading from "./Loading";
import io from "socket.io-client";

const styles = theme => ({
    root: {
        width: 500
    },
    json: {
        overflow: 'auto'
    },
    grid: {
        flexGrow: 1,
        padding: theme.spacing(4),
        height: '50%'
    },
    flex: {
        display: "flex",
        alignItems: "center"
    },
    chatWindow: {
        //padding:"20px"
    },
    msgBox:{
        width:"85%"
    }


});

const socket = io("http://localhost:3000", {
    transports: ["polling","websocket"]
});


function Convochat ({ convo_uid, convoDisplayName, events, currentlySending, classes }) {
    const [values, setValues] = useState({
        msg: "",
        allMessages: [{}],
        activeUsers: [],
        error: false
    });

    //console.log(values);

    const handleChange = event => {
        const {name, value} = event.target
        setValues({
            ...values,
            allMessages:[{}],
            activeUsers:[],
            msg: value,
            error: false
        })
    };

    console.log(values)

    const handleSubmit = event => {
        console.log(values.msg)
        socket.emit("sendmsg", values.msg, convo_uid)
        console.log("sent to socket?")
        setValues({
            ...values,
            msg: "",
            error: false
        })        
    };
     
    function setSocketListeners () {
      socket.on('recmsg', (data) => {
        console.log(data)
        setValues({
            ...values,
            allMessages: data,
            error: false
        })
        console.log(values.activeUsers)
      })

      socket.on('userjoined', (actusers) => {
        setValues({
            ...values,
            activeUsers: actusers,
            error: false
        })
        socket.emit("sendmsg",false,convo_uid)
        console.log("client joined")
        console.log(actusers)
      })

      socket.on('connect', (convo_uid) => {
        console.log("socket connect client!")
        socket.emit("join", convo_uid)
      })

      socket.emit("join", convo_uid)
      socket.emit("sendmsg",false,convo_uid)
    }

    useEffect(() => {
        setSocketListeners()
    }, []);

    console.log(values)

    return (
    <Grid item xs={8}>
        <Grid 
        container
        spacing={2}>
            <Grid item xs={8}>
                <Card>
                    <CardHeader title={convoDisplayName}/>
                    <Divider/>
                    <CardContent>
                        <Grid
                        container
                        direction="column"
                        spacing={2}
                        className={classes.chatWindow}>
                            <Grid item xs>
                                {values.allMessages.map( (message, i)  => {
                                    return (
                                        <div 
                                        className={classes.flex} 
                                        key={i}>
                                            <Typography variant="p">
                                                {message.timestamp}
                                            </Typography>
                                            <Chip 
                                            label={message.msgName} 
                                            className={classes.chip}/>
                                            <Typography variant="p">
                                                {message.msgtext}
                                            </Typography>
                                        </div>
                                    )
                                })}
                            </Grid>
                            <Divider/>
                            <Grid item sm
                            className={classes.flex}>
                                <TextField
                                    className={classes.msgBox}
                                    id="msg-textfield"
                                    label="Input message"
                                    multiline
                                    rowsMax="4"
                                    onChange={handleChange}
                                    variant="outlined"
                                    placeholder="say something! :D"
                                    onKeyPress={(event) => {
                                        if (event.key === 'Enter') {
                                            handleSubmit()
                                        }
                                    }}
                                    value={values.msg}
                                />
                                <Button
                                    type="submit"
                                    variant="contained"
                                    color="primary"
                                    onClick={handleSubmit}>
                                    Send
                                </Button>
                            </Grid>
                        </Grid>
                    </CardContent>
                    <CardActions>

                    </CardActions>
                </Card>
            </Grid>
            <Grid item xs={4}>
                <Card>
                    <CardContent>
                        <Grid
                        container
                        direction="column"
                        alignContent="center"
                        alignItems="center"
                        spacing={2}>
                            <Grid item xs={12}>
                                <Button 
                                variant="contained" 
                                color="primary">
                                    Click Me! Join Videochat!
                                </Button>
                            </Grid>
                            <Grid item xs={12}>
                                <Divider/>
                                <Typography variant="h5" component="h2">
                                    Active Chat Members
                                </Typography>
                                {values.activeUsers.map( (activeuser, i)  => {
                                    return (
                                        <div 
                                        className={classes.flex} 
                                        key={i}>
                                            <Chip 
                                            label={activeuser} 
                                            className={classes.chip}/>
                                        </div>
                                    )
                                })}

                            </Grid>
                        </Grid>
                    </CardContent>
                    <CardActions>

                    </CardActions>
                </Card>
            </Grid>
        </Grid>
    </Grid>
    )
  }


export default withStyles(styles)(Convochat);