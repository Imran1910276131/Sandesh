export const initialstate = {
    profile: null,
};

export const reducer = (state, action) => {
    switch (action.type) {
        case "ADD_PROFILE":
            return {
                ...state,
                profile: action.value,
            };
        case "UPDATE_PROFILE":
            return {
                ...state,
                profile: {
                    ...state.profile,
                    user: {
                        ...state.profile.user,
                        ...action.payload,
                    },
                },
            };
        case "UPDATE_PROFILE_IMAGE":
            return {
                ...state,
                profile: {
                    ...state.profile,
                    image: action.payload,
                },
            };
        default:
            return state;
    }
};
