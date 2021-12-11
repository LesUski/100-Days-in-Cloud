import React from 'react';
import VoteApp from './VoteApp';
import { shallow } from 'enzyme';

describe('<VoteApp />', () => {
  it('renders 1 <VoteApp /> component', () => {
    const component = shallow(<VoteApp />);
    expect(component).toHaveLength(1);
  });
});
