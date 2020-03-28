export const CHANGE_FORM = 'CHANGE_FORM';
export const SET_AUTH = 'SET_AUTH';
export const SENDING_REQUEST = 'SENDING_REQUEST';
export const LOADING_AUTH = 'LOADING_AUTH';
export const SET_ERROR_MESSAGE = 'SET_ERROR_MESSAGE';
export const SET_DATA = 'SET_DATA';
export const SET_ORG_DATA = 'SET_ORG_DATA';

export const login = (username, password) => {
    return dispatch => {
        dispatch(sendingRequest(true));
        dispatch(setErrorMessage(''));
        fetch('/login', {
            method: 'POST',
            body: JSON.stringify({ username, password })
        }).then(res => {
            if (res.ok) return res.json();
            else throw new Error(res.statusText)
        }).then(data => {
            dispatch(sendingRequest(false))
            dispatch(setAuthState(true))
        }).catch(error => {
            dispatch(sendingRequest(false))
            dispatch(setErrorMessage('Login failed'))
        });
    }
}

export const loadData = (path, name) => {
    return dispatch => {
        dispatch(sendingRequest(true))
        dispatch(setErrorMessage(''))
        api(`${path}`)
            .then(data => {
                dispatch(sendingRequest(false))
                dispatch(setData({[name]: data.message}))
            })
            .catch(error => {
                dispatch(sendingRequest(false))
                dispatch(setErrorMessage('Error loading data'))
                if (error.message === '401') {
                    dispatch(setAuthState(false))
                }
            })
    }
}

export const changeData = (path, new_data, updatePaths, updateNames) => {
    return dispatch => {
        dispatch(sendingRequest(true))
        dispatch(setErrorMessage(''))
        fetch(`${path}`, {
            method: 'POST',
            body: JSON.stringify({ new_data })
        }).then(res => {
            if (res.ok) return res.json();
            else throw new Error(res.statusText)
        }).then(data => {
            dispatch(sendingRequest(false))
            {updatePaths.map(function(e, i) {
                dispatch(loadData(e, updateNames[i]))
            })}
        }).catch(error => {
            dispatch(sendingRequest(false))
            dispatch(setErrorMessage('Change data failed'))
        });
    }
}

export const loadOrgData = (path, name) => {
    return dispatch => {
        dispatch(sendingRequest(true))
        dispatch(setErrorMessage(''))
        api(`${path}`)
            .then(data => {
                dispatch(sendingRequest(false))
                dispatch(setOrgData({[name]: data.message}))
            })
            .catch(error => {
                dispatch(sendingRequest(false))
                dispatch(setErrorMessage('Error loading data'))
            })
    }
}

export const changeOrgData = (path, new_data, updatePaths, updateNames) => {
    return dispatch => {
        dispatch(sendingRequest(true))
        dispatch(setErrorMessage(''))
        fetch(`${path}`, {
            method: 'POST',
            body: JSON.stringify({ new_data })
        }).then(res => {
            if (res.ok) return res.json();
            else throw new Error(res.statusText)
        }).then(data => {
            dispatch(sendingRequest(false))
            {updatePaths.map(function(e, i) {
                dispatch(loadOrgData(e, updateNames[i]))
            })}
        }).catch(error => {
            dispatch(sendingRequest(false))
            dispatch(setErrorMessage('Change data failed'))
        });
    }
}

export const loadMe = () => {
    return dispatch => {
        dispatch(loadingAuth(true));
        dispatch(setErrorMessage(''));
        api('/me')
            .then(data => {
            dispatch(loadingAuth(false))
            dispatch(setAuthState(data.isLoggedIn))
        })
            .catch(error => {
                dispatch(loadingAuth(false))
            })
    }
}

export const logout = () => {
    return dispatch => {
        dispatch(sendingRequest(true))
        dispatch(setErrorMessage(''))
        api('/logout')
            .then(data => {
                dispatch(sendingRequest(false))
                dispatch(setAuthState(data.isLoggedIn))
            })
            .catch(error => {
                dispatch(sendingRequest(false))
                dispatch(setErrorMessage('Error logging out'))
            })
    }
}

export const setErrorMessage = message => {
  return { type: SET_ERROR_MESSAGE, message }
}

export const changeForm = newState => {
  return { type: CHANGE_FORM, newState }
}

const setAuthState = newState => {
  return { type: SET_AUTH, newState }
}

const sendingRequest = sending => {
  return { type: SENDING_REQUEST, sending }
}

const loadingAuth = sending => {
  return { type: LOADING_AUTH, sending }
}

const setData = data => {
  return { type: SET_DATA, data }
}

const setOrgData = data => {
  return { type: SET_ORG_DATA, data }
}

const api = path => {
  return fetch(path, { credentials: 'same-origin' }).then(res => {
    if (res.ok) return res.json()
    else throw new Error(res.status)
  })
}