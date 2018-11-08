package src;
import java.io.FileReader;

import org.json.*;

import com.sun.javafx.geom.Point2D;

import jdk.nashorn.internal.parser.JSONParser;



public class Problem {
	private String pathToJson = "../configs/basic_problem_1.json";
	private Point2D[] fields_limits;
	private Point2D[] goalsPosts;
	private int [] goalDirection;
	private Point2D[] opponents;
	private int robot_radius;
	private int theta_step;
	private int pos_step;
	
	public Problem(String pathToJson) throws JSONException {
		
		JSONParser parser = new JSONParser();
		 
        try {
 
            Object obj = parser.parse(new FileReader(
                    "/Users/<username>/Documents/file1.txt"));
 
            JSONObject jsonObject = (JSONObject) obj;
		JSONObject obj = new JSONObject(pathToJson);
		for (int i =0; i<2; i +=2) {
			JSONArray tab = obj.getJSONArray("fields_limits");
			System.out.println(tab);
			fields_limits[i].setLocation(tab.getInt(i), tab.getInt(i+1)); 
		}
		String hello = JsonPath.read(json, "$.data.data2.value");

		robot_radius = obj.getInt("robot_radius");
		theta_step = obj.getInt("theta_step");
		pos_step = obj.getInt("pos_step");
		
        } catch (Exception e) {
            e.printStackTrace();
        }
	}

	public String getPathToJson() {
		return pathToJson;
	}

	public void setPathToJson(String pathToJson) {
		this.pathToJson = pathToJson;
	}

	public Point2D[] getFields_limits() {
		return fields_limits;
	}

	public void setFields_limits(Point2D[] fields_limits) {
		this.fields_limits = fields_limits;
	}

	public Point2D[] getGoalsPosts() {
		return goalsPosts;
	}

	public void setGoalsPosts(Point2D[] goalsPosts) {
		this.goalsPosts = goalsPosts;
	}

	public int[] getGoalDirection() {
		return goalDirection;
	}

	public void setGoalDirection(int[] goalDirection) {
		this.goalDirection = goalDirection;
	}

	public Point2D[] getOpponents() {
		return opponents;
	}

	public void setOpponents(Point2D[] opponents) {
		this.opponents = opponents;
	}

	public int getRobot_radius() {
		return robot_radius;
	}

	public void setRobot_radius(int robot_radius) {
		this.robot_radius = robot_radius;
	}

	public int getTheta_step() {
		return theta_step;
	}

	public void setTheta_step(int theta_step) {
		this.theta_step = theta_step;
	}

	public int getPos_step() {
		return pos_step;
	}

	public void setPos_step(int pos_step) {
		this.pos_step = pos_step;
	}
}
