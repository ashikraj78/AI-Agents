from flask import Flask, render_template, request, jsonify
import traceback
import logging
import sys
from test_research import test_research_topic   
from customer_support_agent import customer_support_agent
from customer_outreach_agent import customer_outreach_agent
# Configure logging to show more detailed information
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/research', methods=['POST'])
def research():
    logger.info("Starting research request...")
    topic = request.form.get('topic')
    
    if not topic:
        logger.warning("No topic provided in request")
        return jsonify({'error': 'No topic provided'}), 400
    
    logger.info(f"Researching topic: {topic}")
    print(f"Researching ashik topic: {topic}")
    
    try:
        # result = test_research_topic(topic)
        # result = customer_support_agent(topic)
        result = customer_outreach_agent(topic)
        logger.info("Research completed successfully")
        return jsonify({
            'success': True,
            'result': result
        })
    except Exception as research_error:
        logger.error(f"Error in research_topic function: {str(research_error)}")
        logger.error(f"Research error traceback: {traceback.format_exc()}")
        return jsonify({
            'success': False,
            'error': f"Error in research_topic: {str(research_error)}"
        }), 500
    
    

if __name__ == '__main__':
    app.run(debug=True) 


