import {
    CHANGE_FORM,
    SET_AUTH,
    SET_NEW_USER,
    SENDING_REQUEST,
    LOADING_AUTH,
    SET_ERROR_MESSAGE,
    SET_DATA,
    SET_ORG_DATA
} from './actions'

const initialState = {
  formState: {
    displayName: '',
    state: '',
    country: ''
  },
  currentlySending: false,
  loadingAuth: false,
  loggedIn: false,
  newUser: false,
  errorMessage: '',
  data: {
    profile: {
      name: '',
      displayName: '',
      state: '',
      country: '',
      avatar: '',
      majors: []
    },
    upcomingEvents: [],
    conversations: [],
    availEvents: [],
    organizations: [],
    allOrganizations: []
  },
  orgData: {
    profile: {},
    upcomingEvents: [],
    conversations: [],
    availEvents: []
  }
}

export const homeReducer = (state = initialState, action) => {
  switch (action.type) {
    case CHANGE_FORM:
      return changeForm(state, action)
    case SET_AUTH:
      return setAuth(state, action)
    case SET_NEW_USER:
      return setNewUser(state, action)
    case SENDING_REQUEST:
      return sendingRequest(state, action)
    case LOADING_AUTH:
      return loadingAuth(state, action)
    case SET_ERROR_MESSAGE:
      return setErrorMessage(state, action)
    case SET_DATA:
      return setData(state, action)
    case SET_ORG_DATA:
      console.log(action)
      return setOrgData(state, action)
    default:
      return state
  }
}

const changeForm = (state, action) => {
  return {
    ...state,
    formState: {
      ...state.formState,
      ...action.newState
    }
  }
}

const setAuth = (state, action) => {
  return {
    ...state,
    loggedIn: action.newState
  }
}

const setNewUser = (state, action) => {
  return {
    ...state,
    newUser: action.newState
  }
}

const sendingRequest = (state, action) => {
  return {
    ...state,
    currentlySending: action.sending
  }
}

const loadingAuth = (state, action) => {
  return {
    ...state,
    loadingAuth: action.sending
  }
}

const setErrorMessage = (state, action) => {
  return {
    ...state,
    errorMessage: action.message
  }
}

const setData = (state, action) => {
  return {
    ...state,
    data: {
      ...state.data,
      ...action.data
    }
  }
}

const setOrgData = (state, action) => {
  return {
    ...state,
    orgData: {
      ...state.orgData,
      ...action.data
    }
  }
}