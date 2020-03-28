import React, {useEffect} from 'react';
import { connect } from 'react-redux';
import { changeForm } from "../actions";
import { TextField } from "@material-ui/core";

function FormTextField({ formState, changeForm, name, value, children, ...rest }) {
    const handleChange = event => {
        changeForm({ [event.target.name]: event.target.value })
    };

    console.log(formState);

    useEffect(() => {
        changeForm({ [name]: value})
    }, []);

    return (
        <TextField {...rest} name={name} value={formState[name]} onChange={handleChange}>
            {children}
        </TextField>
    )
}

const mapStateToProps = state => ({
    formState: state.formState
});

const mapDispatchToProps = dispatch => ({
    changeForm: values => dispatch(changeForm(values))
});

export default connect(mapStateToProps, mapDispatchToProps)(FormTextField);