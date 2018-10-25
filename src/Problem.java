package src;
import org.json.*;
import org.json.JSONException;
import org.json.JSONObject;

import com.sun.javafx.geom.Point2D;



public class Problem {
	private String pathToJson = "../configs/basic_problem_1.json";
	private Point2D[][] fields_limits;
	private int[][] goalsPosts;
	private int [] goalDirection;
	private Opponents opponents;
	private int robot_radius;
	private int theta_step;
	private int pos_step;
	
	public Problem(String pathToJson) throws JSONException {
		JSONObject obj = new JSONObject(pathToJson);
		//fields_limits = obj.getInt("fields_limits");
		//opponents.setX();
		
		robot_radius = obj.getInt("robot_radius");
		theta_step = obj.getInt("theta_step");
		pos_step = obj.getInt("pos_step");
	}

	public String getPathToJson() {
		return pathToJson;
	}

	public void setPathToJson(String pathToJson) {
		this.pathToJson = pathToJson;
	}

	public int[][] getFields_limits() {
		return fields_limits;
	}

	public void setFields_limits(int[][] fields_limits) {
		this.fields_limits = fields_limits;
	}

	public int[][] getGoalsPosts() {
		return goalsPosts;
	}

	public void setGoalsPosts(int[][] goalsPosts) {
		this.goalsPosts = goalsPosts;
	}

	public int[] getGoalDirection() {
		return goalDirection;
	}

	public void setGoalDirection(int[] goalDirection) {
		this.goalDirection = goalDirection;
	}

	public int[] getOpponents() {
		return opponents;
	}

	public void setOpponents(int[] opponents) {
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
