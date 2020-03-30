import React, {useState, useEffect} from 'react';
import {Button, Card, CardContent, CardHeader, Divider, List, Menu, ListItem, MenuItem, TextField} from "@material-ui/core";
import Loading from "../views/Loading";
import MainLayout from "../layouts/MainLayout";
import {Autocomplete} from "@material-ui/lab";
import {Redirect} from "react-router";
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

function SearchBar ({ open, handleClose, all_organizations, currentlySending }) {
    console.log(open);

    const [values, setValues] = useState({
        query: '',
        redirect: false
    });

    const handleSubmit = event => {
        const organizations = all_organizations.filter((e) => e.displayName === values.query);
        if (organizations.length > 0) {
            handleClose();
            setValues({
            ...values,
            redirect: organizations[0].id
        })
        }
    }

    const handleChange = (event, value) => {
        setValues({
            ...values,
            query: value
        })
    }

    // const handleMenuItemClick = (event, displayName) => {
    //     filterList(displayName)
    // }

    if (values.redirect) {
        return <Redirect to={`/organization/${values.redirect}`}/>
    }

    return (
        <div>
            {!currentlySending ?
                <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
                <DialogTitle id="form-dialog-title">Search for an Organization</DialogTitle>
                <DialogContentText>
                    Filter results based on organization name.
                  </DialogContentText>
                    <Autocomplete
                        variant="outlined"
                        options={all_organizations}
                        getOptionLabel={(option) => option.displayName}
                        required
                        renderInput={(params) => <TextField {...params} label="Search" variant="outlined"/>}
                        onInputChange={handleChange}
                    />
                    <Button
                        color="primary"
                        variant="contained"
                        onClick={handleSubmit}
                    >
                        Go!
                    </Button>
                    </Dialog>: <Loading/>}
        </div>
    )
}

export default SearchBar;