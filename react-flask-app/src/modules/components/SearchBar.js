import React, {useState, useEffect} from 'react';
import {Button, Card, CardContent, CardHeader, Divider, List, Menu, ListItem, MenuItem, TextField} from "@material-ui/core";
import Loading from "../views/Loading";
import MainLayout from "../layouts/MainLayout";
import {Autocomplete} from "@material-ui/lab";
import {Redirect} from "react-router";

function SearchBar ({ all_organizations, currentlySending }) {
    const [values, setValues] = useState({
        query: '',
        redirect: false
    });

    // useEffect(() => {
    //     setValues({
    //         initialItems: all_organizations,
    //         currItems: all_organizations
    //     })
    // }, [all_organizations])
    //
    // const filterList = event => {
    //     const newItems = values.initialItems.filter((organization) => {
    //         console.log(organization);
    //         console.log(event);
    //         return organization.displayName.toLowerCase().search(event.toLowerCase()) !== -1;
    //     });
    //     setValues({
    //         query: event,
    //         currItems: newItems
    //     })
    // }

    const handleSubmit = event => {
        event.preventDefault();
        const organizations = all_organizations.filter((e) => e.displayName === values.query);
        if (organizations.length > 0) {
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
            {!currentlySending ? <MainLayout>
                <Card>
                    <form
                        autoComplete="off"
                        onSubmit={handleSubmit}
                    >
                        <CardHeader
                          subheader="Filter results based on organization name."
                          title="Search for an Organization"
                        />
                        <Divider />
                        <CardContent>
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
                                type="submit"
                            >
                                Go!
                            </Button>
                        </CardContent>
                    </form>
                </Card>
            </MainLayout> : <Loading/>}
        </div>
    )
}

export default SearchBar;