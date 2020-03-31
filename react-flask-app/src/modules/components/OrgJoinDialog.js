import React, {useState, useEffect} from 'react';
import {Button, Card, CardContent, CardHeader, Divider, List, Menu, ListItem, MenuItem, TextField} from "@material-ui/core";
import Loading from "../views/Loading";
import MainLayout from "../layouts/MainLayout";
import {Autocomplete} from "@material-ui/lab";
import { withStyles } from '@material-ui/core/styles';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

const styles = theme => ({
    root: {
        padding: theme.spacing(4)
    }
})

function OrgJoinDialog ({ passcode, joinOrganization, open, handleClose, classes }) {
    const [query, setQuery] = useState("");
    const [error, setError] = useState(false);

    const handleSubmit = event => {
        console.log(query)
        console.log(passcode)
        if (query === passcode) {
            handleClose();
            joinOrganization();
        }
        else {
            setError(true);
        }
    }

    const handleChange = event => {
        setError(false);
        setQuery(event.target.value)
    }

    // const handleMenuItemClick = (event, displayName) => {
    //     filterList(displayName)
    // }

    // if (values.redirect) {
    //     handleClose();
    //     return <Redirect to={`/organization/${values.redirect}`}/>
    // }

    return (
        <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="form-dialog-title"
            fullWidth
            className={classes.root}
        >
            <DialogTitle id="form-dialog-title">Enter Passcode</DialogTitle>
            <DialogContent>
                <DialogContentText>
                    To join this organization you must enter a valid passcode.
                </DialogContentText>
                <TextField
                    error={error}
                    fullWidth
                    value={query}
                    name={"query"}
                    label={error ? "Incorrect passcode" : "Passcode"}
                    variant="outlined"
                    margin="dense"
                    onChange={handleChange}
                />
            </DialogContent>
            <DialogActions>
                <Button
                color="primary"
                variant="contained"
                onClick={handleSubmit}
            >
                Submit
            </Button>
            </DialogActions>
        </Dialog>
    )
}

export default withStyles(styles)(OrgJoinDialog);