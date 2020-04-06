import React, {useState, useEffect } from "react";
import Button from "@material-ui/core/Button";
import Icon from '@material-ui/core/Icon';
import MainLayout from "../layouts/MainLayout";
import { TextField } from "@material-ui/core";
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
    }
});


function Testchat ({ socket }) {

    const [values, setValues] = useState({
        msg: "",
        error: false
    });

    const handleChange = event => {
        setValues({
            msg: event.target.value,
            error: false
        })
    };

    const handleSubmit = event => {
        console.log(values.msg)
        socket.emit("connect")
        socket.emit("message")
        console.log("sent to socket?")
    };

    return (
        <div>
            <TextField
                id="msg-textfield"
                error={values.error}
                multiline
                rowsMax="4"
                onChange={handleChange}
                variant="outlined"
                margin="dense"
            />
            <Button
                variant="contained"
                color="primary"
                onClick={handleSubmit}>
                Send
            </Button>
        </div>
    )
}

export default withStyles(styles)(Testchat);