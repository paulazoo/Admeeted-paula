import React, {useState} from "react";
import Button from "@material-ui/core/Button";
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
    Grid
} from "@material-ui/core";
import { withStyles } from '@material-ui/core/styles';
import ReactJson from "react-json-view";
import Loading from "./Loading";


const styles = theme => ({
    root: {
        width: 500
    },
    json: {
        overflow: 'auto'
    }
});

function Master ({ events, currentlySending, generateConvos, classes }) {
    const [values, setValues] = useState({
        convo_name: "",
        event_uid: "",
        error: false
    });

    console.log(values);

    const handleSubmit = event => {
        if (values.event_uid.length > 0 && values.convo_name.length > 0) {
            generateConvos(values.event_uid, values.convo_name);
        } else {
            setValues({
                ...values,
                error: true
            })
        }
    };

    const handleChange = event => {
        setValues({
            ...values,
            [event.target.name]: event.target.value,
            error: false
        })
    };

    function showEventDetails() {
        const selectedEvent = events.filter((event) => event.id === values.event_uid)[0];
        return (
            <ReactJson collapsed src={selectedEvent}/>
        )
    }

    return (
        <div>
            {!currentlySending ? <MainLayout>
                <Grid container spacing={4}>
                    <Grid item md={6} xs={12}>
                        <Card className={classes.root}>
                            <CardHeader title={"Generate Conversations"}/>
                            <Divider/>
                            <CardContent>
                                <FormControl
                                    error={values.error}
                                    fullWidth
                                    variant={"outlined"}
                                >
                                    <InputLabel>Event Name</InputLabel>
                                    <Select
                                        value={values.event_uid}
                                        required
                                        name={"event_uid"}
                                        onChange={handleChange}
                                    >
                                        {events.map((event) => {
                                            return <MenuItem value={event.id}>{event.displayName}</MenuItem>
                                        })}
                                    </Select>
                                </FormControl>
                                {values.event_uid ? showEventDetails() : null}
                                <TextField
                                    fullWidth
                                    error={values.error}
                                    value={values.convo_name}
                                    name={"convo_name"}
                                    label={"Conversation Name"}
                                    variant="outlined"
                                    margin="dense"
                                    onChange={handleChange}
                                />
                            </CardContent>
                            <CardActions>
                                <Button
                                    color="primary"
                                    variant="contained"
                                    onClick={handleSubmit}>
                                    Generate
                                </Button>
                            </CardActions>
                        </Card>
                    </Grid>
                </Grid>
            </MainLayout> : <Loading/>}
        </div>
    )
}

export default withStyles(styles)(Master);