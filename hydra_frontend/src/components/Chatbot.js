import { useState } from 'react';
import { Button, Input, Layout, List, Modal, Typography, Avatar } from 'antd';
import { UserOutlined, RobotOutlined, QuestionCircleOutlined } from '@ant-design/icons';
import Robot from './Robot';

const { Content } = Layout;
const { TextArea } = Input;
const { Text } = Typography;

const Chatbot = () => {
  let isRobot = false;
  const uid = localStorage.getItem('uid');
  const cid = localStorage.getItem('cid');
  const [messages, setMessages] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);
  const [inputValue, setInputValue] = useState('');
  const handleModalClick = () => {
    setModalVisible(true);
  };

  const handleModalClose = () => {
    setModalVisible(false);
  };

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSendMessage = () => {
    if (inputValue.trim()) {
     
      setTimeout(() => {
        setMessages([...messages, { message: inputValue.trim(), isRobot: false }]);
        setInputValue('');
      }, 500);
      setTimeout(() => {

        // setMessages((prevMessages) => [
        //   ...prevMessages,
        //   { message: 'Sorry I cannot understand', isRobot: true },
        // ]);
        handleSubmit(inputValue.trim());

      }, 1000);
     
    }
    // console.log(messages);
  };
  const handleSubmit = (message) => {
    fetch(`http://localhost:8000/chatbot/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({'cid': cid, 'message': message}),
    }).then(async(response) => {
        const jsonRes = await response.json();
        console.log(jsonRes);
        if (response.status !== 200) {
            message.error(jsonRes.error);
            return;
        }
        console.log('response is',jsonRes);
        setMessages((prevMessages) => [
          ...prevMessages,
          { message: jsonRes.message, isRobot: true },
        ]);
     
    })
    
  };

  return (
    <>
      <Button style={{border: 'none',
        backgroundColor: '#f1f1f1',
        padding: '10px', transform: 'scale(1.5)'}} icon={<QuestionCircleOutlined size='300px'/>} onClick={handleModalClick}>
       
      </Button>
      <Modal
        title="Chat Window"
        open={modalVisible}
        onCancel={handleModalClose}
        footer={null}
      >
        <Layout>
          <Content style={{ overflow: 'auto', height: '500px' }}>
          <div>
            <Robot />
            <List
              itemLayout="horizontal"
              dataSource={messages}
              renderItem={(item) => (
                <List.Item
                  style={{borderBlockEnd: 'none'}}
                  key={item.message}>
                    {item.isRobot ? (
                      <List.Item.Meta
                      avatar={
                        <Avatar style={{ backgroundColor: '#87d068' }} icon={<RobotOutlined />} />
                      }
                      title={'Robot'}
                      description={item.message}
                    />) : (  
                      <List.Item.Meta
                    avatar={
                      <Avatar style={{ backgroundColor: '#fffff' }} icon={<UserOutlined />} />
                    }
                    title={'You'}
                    description={item.message}
                  />)}
                  
                </List.Item>
              )}
            />
         
            
          </div>
          </Content>
          <Content>
            <div style={{display: 'flex', flexDirection: 'row'}}>
              <TextArea
                value={inputValue}
                onChange={handleInputChange}
                rows={4}
                style={{ display: "inline-block", height: "30px" }}
              />
              <Button style={{display: "inline-block", height: "30px", marginLeft: '3px' }} type='primary' onClick={handleSendMessage}>
                Send
              </Button>
            </div> 
          </Content>
        </Layout>
      </Modal>
    </>
  
  );
};

export default Chatbot;