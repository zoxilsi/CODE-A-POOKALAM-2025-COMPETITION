
from turtle import * 
import math

def draw_ring_beads(cx, cy, radius, count, size, clr):
	"""Draw a ring of evenly spaced dots (beads)."""
	penup()
	setheading(0)
	for i in range(count):
		ang = 360.0 * i / count
		x = cx + radius * math.cos(math.radians(ang))
		y = cy + radius * math.sin(math.radians(ang))
		goto(x, y)
		dot(size, clr)

def draw_lotus(cx, cy, petal_count, inner_r, outer_r, fill_main, fill_shadow=None):
	"""Draw a radial lotus rosette using two circle arcs per petal."""
	penup()
	for i in range(petal_count):
		ang = 360.0 * i / petal_count
		setheading(ang)
		goto(cx, cy)
		forward(inner_r)
		left(90)
		if fill_shadow:
			# subtle shadow underlay
			fillcolor(fill_shadow)
			begin_fill()
			circle(outer_r, 65)
			left(115)
			circle(outer_r, 65)
			end_fill()
			right(90)
		# main petal
		fillcolor(fill_main)
		begin_fill()
		circle(outer_r, 60)
		left(120)
		circle(outer_r, 60)
		end_fill()
		right(90)

def draw_gradient_background(start_color, end_color, radius, step=6):
	"""Draw a soft radial gradient behind the pookalam (draw first)."""
	penup()
	goto(0, 0)
	colormode(255)
	R = int(radius)
	for r in range(R, 0, -step):
		t = r / float(R)
		color = (
			int(start_color[0] * t + end_color[0] * (1 - t)),
			int(start_color[1] * t + end_color[1] * (1 - t)),
			int(start_color[2] * t + end_color[2] * (1 - t)),
		)
		pencolor(color)
		dot(r * 2)
	pencolor("black")

def calculate_arc_dimensions(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    width = 2 * radius * math.sin(angle_radians / 2)
    height = radius - radius * math.cos(angle_radians / 2)
    return width, height
def find_triangle_height_and_base(a, theta_degrees):
    theta_radians = math.radians(theta_degrees)
    h = a * math.sin(theta_radians)
    b = 2 * math.sqrt(a**2 - h**2)
    return h, b
def calculate_arc_dimensions(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    width = 2 * radius * math.sin(angle_radians / 2)
    height = radius - radius * math.cos(angle_radians / 2)
    return width, height
def calculate_arc_radius_and_angle(width, height):
    half_width = width / 2
    radius = math.sqrt(half_width**2 + height**2)
    angle_rad = 2 * math.atan(half_width / height)
    angle_deg = math.degrees(angle_rad)
    return radius, angle_deg
def draw_pentagon(x, y, side_length,pen_down=False,fillclr=None):
		penup()
		angle = 360 / 6
		h,a = find_triangle_height_and_base(side_length,angle)
		goto(x-side_length/2, y-a)
		if pen_down:pendown()
		
		if fillclr is not None:
				fillcolor(fillclr)
				begin_fill()
		for _ in range(5):
			forward(side_length)
			left(angle)
		if fillclr is not None:end_fill()
def draw_eye(x,y,major,minor,fillclr=None,pen_down=True):
	goto(x,y)
	penup()
	x_diff,_ = calculate_arc_dimensions(minor,90)
	penup()
	left(45)
	forward(major*0.02)
	y_center = pos()[1]
	x_center = x + (x_diff /2)
	goto(x_center,y_center)#-major)
	if pen_down:pendown()
	if fillclr is not None:
		fillcolor(fillclr)
		begin_fill()
	for _ in range(2):
		# circle(major,90)
		chead = heading()
		forward(major*0.02)
		left(60)
		forward(major*0.02)
		setheading(chead+90)
		circle(minor,90)
	if fillclr is not None:end_fill()
def draw_dual_circle(x,y,rad,gap,fillclr,upper_size=3):
  penup()
  goto(x,y-rad-gap)
  setheading(0)
  fillcolor(fillclr)
  begin_fill()
  circle(rad-gap)
  end_fill()
  right(90)
  forward(gap)
  setheading(0)
  color(fillclr)
  pensize(upper_size)
  pendown()
  circle(rad)
  penup()
  color('#000')
def draw_dashed_circle(x,y,rad,fillclr,peaces=10):
  penup()
  goto(x,y-rad)
  setheading(0)
  fillcolor(fillclr)
  for i in range(1,peaces+1):
    if i%2 == 0:
      cx1,cy1 = pos()
      circle(rad,360/peaces)
      cx2,cy2 = pos()
      chead = heading()
      circle(rad,-360/peaces)
      begin_fill()
      circle(rad,360/peaces)
      goto(x,y)
      goto(cx1,cy1)
      end_fill()
      goto(cx2,cy2)
      setheading(chead)
    else:circle(rad,360/peaces)
def draw_theyyam_face(x,y,height):
	# ellipse_height = height * 0.594
	# ellipse_width = height * 0.451
	eye_pos = height * 0.22
	mouth_pos = height * 0.10
	head_design_pos = height * 0.309
	top_band_pos = height * 0.516
	top_band_height = height * 0.098
	top_band_radius = height * 0.32
	top_band_angle = 95
	penup()
	# kireedam (crown)
	crown_height = height * 0.5
	crown_bottom_width = height * 0.94
	crown_top_circle_gap = height * 0.05
	crown_top_circle_penta_gap = height * 0.1
	goto(x - (crown_bottom_width/2),y+crown_height)
	setheading(90)
	fillcolor('#A01005')
	begin_fill()
	circle(-crown_bottom_width/2,180)
	end_fill()
	# dots
	goto(x - ((crown_bottom_width/2)-(crown_top_circle_gap)),y+crown_height)
	setheading(90)
	num_peaces = 40
	for _ in range(num_peaces):
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap)),180/num_peaces/2)
		dot(height*0.02,'#fff')
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap)),180/num_peaces/2)
	# hexagons
	goto(x - ((crown_bottom_width/2)-(crown_top_circle_gap+crown_top_circle_penta_gap)),y+crown_height)
	setheading(90)
	num_peaces = 4
	for _ in range(num_peaces):
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap+crown_top_circle_penta_gap)),180/num_peaces/2)
		chead = heading()
		setheading(0)
		cx,cy = pos()
		draw_pentagon(cx,cy,height*0.082,fillclr='#FC8505')
		setheading(chead)
		goto(cx,cy)
		setheading(0)
		draw_pentagon(cx,cy,height*0.053,fillclr='#FEA901')
		setheading(chead)
		goto(cx,cy)
		setheading(0)
		draw_pentagon(cx,cy,height*0.037,fillclr='#D51510')
		setheading(chead)
		goto(cx,cy)
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap+crown_top_circle_penta_gap)),180/num_peaces/2)
	setheading(0)
	# dashed circle
	draw_dashed_circle(x,y+crown_height+crown_bottom_width/50,crown_bottom_width/5,'#FCF9FB',50)
	# Draw the face
	face_bottom_circle_ang = 152
	goto(x,y)
	circle(height*0.2196,-face_bottom_circle_ang/2)
	chead = heading()
	tmp_x1,tmp_y1 = pos()
	chead = heading()
	setheading(90)
	forward(top_band_pos - height * 0.16)
	setheading(270)
	fillcolor('#EB5928')
	begin_fill()
	forward(top_band_pos- height * 0.16)
	setheading(chead)
	circle(height*0.2196,face_bottom_circle_ang)
	setheading(90)
	forward(top_band_pos - height * 0.16)
	end_fill()
	#decoration1
	goto(tmp_x1+height*0.005,tmp_y1+height*0.035)
	setheading(chead)
	num_peaces = 9
	for i in range(1,num_peaces):
		j = i if i < num_peaces/2 else num_peaces - i
		crad = (height*0.017) * ((2/num_peaces)*(j%(num_peaces/2)))
		circle(height*0.2196 - height * 0.005,face_bottom_circle_ang/num_peaces)
		tmp_x1,tmp_y1 = pos()
		chead = heading()
		draw_dual_circle(tmp_x1,tmp_y1,crad,gap=crad/2.3,fillclr='#A21300',upper_size=height*0.003)
		setheading(chead)
		goto(tmp_x1,tmp_y1)
	
	# draw the band above face
	goto(x,y+top_band_pos)
	setheading(0)
	pendown()
	circle(-top_band_radius,-top_band_angle/2)
	dec_tmp_x1,dec_tmp_y1 = pos()
	dec_tmp_head1 = heading()
	fillcolor('#7F080C')
	begin_fill()
	circle(-top_band_radius,top_band_angle)
	band_tmp_ang = heading()
	band_circle_pos_x,band_circle_pos_y = pos()
	setheading(90)
	forward(top_band_height)
	setheading(band_tmp_ang+180)
	circle(top_band_radius,top_band_angle)
	setheading(270)
	forward(top_band_height)
	band_circle_pos_x1,band_circle_pos_y1 = pos()
	end_fill()
	band_side_circle_rad = height*0.085
	penup()
	#decorations
	# outside
	goto(dec_tmp_x1,dec_tmp_y1- height * 0.02)
	setheading(dec_tmp_head1)
	num_dots = 50
	for _ in range(num_dots):
		dot(height*0.005,'#FFf')
		circle(-top_band_radius,top_band_angle/num_dots)
	# inside
	for i in range(1,3):
		goto(dec_tmp_x1,dec_tmp_y1 + ((top_band_height/3)*i))
		setheading(dec_tmp_head1)
		num_dots = 20
		for _ in range(num_dots):
			dot(height*0.02,'#FF9002')
			circle(-top_band_radius,top_band_angle/num_dots)
	
	# draw the side circle in the band
	goto(band_circle_pos_x1,band_circle_pos_y1+(band_side_circle_rad - top_band_height))
	setheading(0)
	fillcolor('#6E1109')
	begin_fill()
	circle(band_side_circle_rad)
	end_fill()
	# decoirations
	setheading(90)
	forward(height*0.054)
	setheading(0)
	fillcolor('#EB5928')
	begin_fill()
	circle(band_side_circle_rad - height*0.054)
	end_fill()
	setheading(270)
	# decorations
	forward(height * 0.027)
	setheading(0)
	num_dots = 13
	for _ in range(num_dots):
		circle((band_side_circle_rad - height * 0.027),360/num_dots)
		dot(height*0.02,'#FF9002')

	goto(band_circle_pos_x,band_circle_pos_y+(band_side_circle_rad - top_band_height))
	setheading(0)
	fillcolor('#6E1109')
	begin_fill()
	circle(band_side_circle_rad)
	end_fill()
	setheading(90)
	forward(height*0.054)
	setheading(0)
	fillcolor('#EB5928')
	begin_fill()
	circle(band_side_circle_rad - height*0.054)
	end_fill()
	setheading(270)
	forward(height * 0.027)
	setheading(0)
	num_dots = 13
	for _ in range(num_dots):
		circle((band_side_circle_rad - height * 0.027),360/num_dots)
		dot(height*0.024,'#FF9002')
	
	# lips
	goto(x,y+mouth_pos)
	setheading(0)
	lip_bottom_rad = height * 0.087
	lip_bottom_ang = 93
	fillcolor('#A60F06')
	circle(lip_bottom_rad,-lip_bottom_ang/2)
	tmp_x1,tmp_y1 = pos()
	chead = heading()
	begin_fill()
	circle(lip_bottom_rad,lip_bottom_ang)
	tmp_x2,tmp_y2 = pos()
	chead2 = heading()
	end_fill()
	fillcolor('#7C0808')
	goto(tmp_x1,tmp_y1)
	setheading(360-chead)
	begin_fill()
	circle(-lip_bottom_rad/2,lip_bottom_ang)
	end_fill()
	goto(tmp_x2,tmp_y2)
	setheading(360-chead2)
	begin_fill()
	circle(-lip_bottom_rad/2,-lip_bottom_ang)
	end_fill()
	# eyes
	eye_gap = height * 0.121
	eye_bottom_rad = 	height * 0.101
	eye_bottom_angle = 114
	eye_eye_gap = height * 0.046
	eye_right_cir_rad = height * 0.075
	eye_right_cir_ang = 106
	goto(x-eye_gap,y+eye_pos)
	setheading(0)
	circle(eye_bottom_rad,-eye_bottom_angle/2)
	chead = heading()
	left(80)
	circle(eye_right_cir_rad,eye_right_cir_ang)
	fillcolor('#382030')
	begin_fill()
	left(180)
	circle(-eye_right_cir_rad,eye_right_cir_ang)
	setheading(chead)
	tmp_x1,tmp_y1 = pos()
	tmp_head = heading()
	circle(eye_bottom_rad,eye_bottom_angle)
	left(110)
	eye_left_cir_rad = height * 0.1793
	eye_left_cir_ang = 42
	circle(-eye_left_cir_rad,eye_left_cir_ang)
	end_fill()
	setheading(0)
	draw_eye(x-eye_gap,tmp_y1,height*0.03,height*0.06,fillclr='#fff',pen_down=False)
	goto(x-eye_gap,tmp_y1-height*0.015)
	setheading(0)
	fillcolor('#5A3137')
	begin_fill()
	circle(height*0.015)
	end_fill()
	goto(x-eye_gap,tmp_y1-height*0.005)
	setheading(0)
	fillcolor('#EEE5E6')
	begin_fill()
	circle(height*0.005)
	end_fill()
	#decorations left eye
	setheading(tmp_head)
	goto(tmp_x1,tmp_y1-height * 0.02)
	num_peaces = 10
	for _ in range(num_peaces):
		circle(eye_bottom_rad,eye_bottom_angle/num_peaces)
		dot(height * 0.009,'#fff')
	# eye right
	goto(x+eye_gap,y+eye_pos)
	setheading(0)
	circle(eye_bottom_rad,eye_bottom_angle/2)
	chead = heading()
	left(100)
	circle(-eye_right_cir_rad,eye_right_cir_ang)
	color('pink')
	fillcolor('#382030')
	begin_fill()
	left(180)
	circle(eye_right_cir_rad,eye_right_cir_ang)
	setheading(chead)
	tmp_x1,tmp_y1 = pos()
	tmp_head = heading()
	circle(eye_bottom_rad,-eye_bottom_angle)
	left(70)
	eye_left_cir_rad = height * 0.1793
	eye_left_cir_ang = 42
	circle(eye_left_cir_rad,eye_left_cir_ang)
	end_fill()
	setheading(0)
	draw_eye(x+eye_gap,tmp_y1,height*0.03,height*0.06,fillclr='#fff',pen_down=False)
	goto(x+eye_gap,tmp_y1-height*0.015)
	setheading(0)
	fillcolor('#5A3137')
	begin_fill()
	circle(height*0.015)
	end_fill()
	goto(x+eye_gap,tmp_y1-height*0.005)
	setheading(0)
	fillcolor('#EEE5E6')
	begin_fill()
	circle(height*0.005)
	end_fill()
	#decorations right eye
	setheading(tmp_head)
	goto(tmp_x1,tmp_y1-height * 0.02)
	num_peaces = 10
	for _ in range(num_peaces):
		circle(eye_bottom_rad,-eye_bottom_angle/num_peaces)
		dot(height * 0.009,'#fff')
	nose_gap = height * 0.184
	goto(x,y+nose_gap)
	setheading(90)
	pensize(height*0.02)
	pendown()
	color('#9E1205')
	forward(height* 0.081)
	penup()
	angle_top_circles = 95
	top_circles_mul_gap = height * 0.025
	top_circles_gap = height * 0.364
	 # draw the two brown half circles in the top of the face
	goto(x,y+top_circles_gap)
	fillcolor('#9E1205')
	setheading(0)
	circle(-height * 0.1,-angle_top_circles/2)
	tmp_x1,tmp_y1 = pos()
	chead2 = heading() # angle for future use (RIGHT, BOTTOM)
	begin_fill()
	chead1 = heading()
	circle(-height * 0.1,angle_top_circles)
	chead = heading() # angle for future use (LEFT, BOTTOM)
	left(90)
	forward(height*0.01)
	setheading(chead+180)
	circle(height * 0.1+height*0.01,angle_top_circles)
	end_fill()
	# second top brown half circle
	setheading(chead1)
	left(90)
	forward(height*0.067)
	right(90)
	begin_fill()
	circle(-(height * 0.1 + height*0.067),angle_top_circles)
	chead = heading()
	left(90)
	forward(height*0.01)
	setheading(chead+180)
	circle(height * 0.1 + height*0.067 + height * 0.01,angle_top_circles)
	end_fill()
	
	#Fill white 
	goto(tmp_x1,tmp_y1)
	setheading(chead2)
	fillcolor('#fff')
	begin_fill()
	circle(-height * 0.1,angle_top_circles)
	end_fill()
	# top dot dot
	setheading(chead2)
	goto(tmp_x1,tmp_y1)
	left(90)
	forward(height*0.05) # go forward
	right(90)
	num_peaces = 20
	for _ in range(num_peaces-1):
		circle(-(height * 0.1 + height*0.05),angle_top_circles/num_peaces)
		dot(height * 0.005,'#fff')
	
def colored_star(x,y,size=40,fillclr=None,angle=120,pen_down=False):
	penup()
	chead = heading()
	goto(x,y)
	setheading(60)
	angle = 120
	forward(size)
	x_diff1,y_len1 = pos()
	backward(size)
	for _ in range(2):
		forward(size)
		right(angle)
		forward(size)
		right(72 - angle)
	forward(size)
	right(angle)
	y_diff,y_len2 = pos()
	height = y_len2 - y_len1
	x_diff = x_diff1 - x
	goto(x+x_diff,y_len1+(height/2))
	x1,y1 = pos()
	x_diff = x - x1
	y_diff = y - y1
	goto(x+x_diff,y+y_diff)
	setheading(60)
	if pen_down:pendown()
	if fillclr is not None:
		fillcolor(fillclr)
		begin_fill()
	for _ in range(5):
		forward(size)
		right(angle)
		forward(size)
		right(72 - angle)
	if fillclr is not None:
		end_fill()
	goto(x,y)
	setheading(chead)
def draw_ellipse(x,y,major,minor,fillclr=None,pen_down=True):
	penup()
	x_diff,y_diff = calculate_arc_dimensions(minor,90)
	y_center = y + (major / 2) - y_diff
	x_center = x + (x_diff /2)
	goto(x_center,y_center)#-major)
	setheading(45)
	if pen_down:pendown()
	if fillclr is not None:
		fillcolor(fillclr)
		begin_fill()
	for _ in range(2):
		circle(major,90)
		circle(minor,90)
	if fillclr is not None:end_fill()
def draw_square(x,y,width,height,angle=0,clr="black",fill=False,border=1,border_clr="black"):
	penup()
	goto(x,y)
	if border > 0:pendown()
	setheading(angle)
	color(border_clr)
	pensize(border)
	if fill:
		fillcolor(clr)
		begin_fill()
	forward(width/2)
	left(90)
	forward(height)
	left(90)
	forward(width)
	left(90)
	forward(height)
	left(90)
	forward(width/2)
	if fill:end_fill()

def draw_theyyam(x,y,width):
	penup()
	setheading(0)
	#some variable used to scale
	non_circle_len = width * 0.20
	len_square_bottom = width * 0.137
	len_half_circle = width * 0.5
	# reset the y and calculate the height of the drawing
	height = non_circle_len + len_square_bottom+len_half_circle#width * 0.67
	y = y - height /2
	# Draw a reference square, avoided on production
	# draw_square(x,y,width,height,fill=True,clr="yellow")
	# goto the position to draw the big circle
	goto(x-width/2,y)
	left(90)
	forward(len_square_bottom+non_circle_len)
	fillcolor("#720B26")
	begin_fill()
	circle(-len_half_circle,180) # top circle
	end_fill()
	fillcolor('#D7140E')
	# Second half circle inside the first on the top
	half_circle_gap = width * 0.093
	penup()
	# got to the perticular position
	setheading(90)
	goto(x-width/2+half_circle_gap,y+(len_square_bottom+non_circle_len))
	begin_fill()
	# second top circle
	circle(-len_half_circle + half_circle_gap,180)
	end_fill()
	# draw the third half circle
	setheading(90)
	goto(x-width/2+half_circle_gap*2,y+(len_square_bottom+non_circle_len))
	fillcolor('#FF5C01')
	begin_fill()
	# third top circle
	circle(-len_half_circle + half_circle_gap*2,180)
	end_fill()
	# designs inside fist half circle
	goto(x-(width/2)+(half_circle_gap/2),y+(len_square_bottom+non_circle_len)) # design position
	setheading(90)
	num_dots = 32
	for _ in range(num_dots - 1):
		circle(-len_half_circle + (half_circle_gap/2),180/num_dots)
		dot(width*0.024,'#FF9002')
	#designs inside second half circle
	goto(x-width/2+half_circle_gap+(width * 0.015),y+(len_square_bottom+non_circle_len))
	setheading(90)
	num_dots = 64
	for _ in range(num_dots - 1):
		circle(-len_half_circle + (half_circle_gap+(width*0.015)),180/num_dots)
		dot(1.5,'#FFF')
	#second 
	goto(x-width/2+(half_circle_gap*2)-(width * 0.015),y+(len_square_bottom+non_circle_len))
	setheading(90)
	num_dots = 64
	for _ in range(num_dots - 1):
		circle(-len_half_circle + ((half_circle_gap*2)-(width*0.015)),180/num_dots)
		dot(1.5,'#FFF')
	goto(x-width/2+(half_circle_gap*1.5),y+(len_square_bottom+non_circle_len))
	setheading(90)
	num_dots = 11
	for _ in range(num_dots - 1):
		circle(-len_half_circle + (half_circle_gap*1.5),180/num_dots)
		cx,cy = pos()
		colored_star(cx,cy,size=width*0.01,fillclr="#FFF")
	center_no_circle_rad = width * 0.19 # the area in the circle which doesnt have any designs
	center_mul_circle_gap = width * (0.061 - 0.006) # last circle multiple doted circle gap
	for i  in range(3):
		goto(x-center_no_circle_rad-(center_mul_circle_gap*i),y+(len_square_bottom+non_circle_len))
		setheading(90)
		num_dots = 30 + (i * 10)
		for _ in range(num_dots - 1):
			circle(-(center_no_circle_rad+(center_mul_circle_gap*i)),180/num_dots)
			dot(width*0.012,'#FF9002')
	# Draw the square below the big half circle
	draw_square(x,y+non_circle_len,width,len_square_bottom,fill=True,clr='#FF5C01',border=0) # bottom_square
	draw_square(x,y+non_circle_len + (width * 0.024),width - (width * 0.015),len_square_bottom - 2*(width * 0.024),fill=True,clr='#720B26',border=0) # bottom_square
	#decoration
	setheading(0)
	goto(x-width/2,y+non_circle_len + (width * 0.012))
	num_peaces = 50
	for _ in range(num_peaces - 1):
		forward(width / num_peaces)
		dot(width*0.012,'#FF9002')
	goto(x-width/2,y+non_circle_len + len_square_bottom - (width * 0.012))
	for _ in range(num_peaces - 1):
		forward(width / num_peaces)
		dot(width*0.012,'#FF9002')
	
	goto(x-(width - (width * 0.015))/2,y+non_circle_len + (width * 0.024) + (len_square_bottom - 2*(width * 0.024))/2)
	setheading(0)
	wi_btm = width - (width * 0.015)
	num_peaces = 8
	for i in range(num_peaces):
		forward(wi_btm/num_peaces/2)
		dot(width * 0.028,'#FE3000')
		setheading(270)
		forward(width *0.031)
		num = 20
		setheading(0)
		for _ in range(num):
			dot(width*0.005,'#FC9103')
			circle(width * 0.031,360/num)
		setheading(90)
		forward(width *0.031)
		setheading(0)
		forward(wi_btm/num_peaces/2)

	#  Some refernces, to scale the image
	bottom_len = width / 2 # width of the lower square, the square below the big square
	bottom_one_height = width * 0.1 # Height of the square
	bottom_band_height = width * 0.115 # height pf the band
	bottom_band_ang = 90 # arc in which the band want to be visible
	# draw reference square, avoided in production
	#draw_square(x,y+(non_circle_len - bottom_one_height),bottom_len,bottom_one_height) # bottom square one
	# radius of the curve in the bottom square with the half width
	bottom_r2 = width * 0.17 / 2
	penup()
	# goto the position
	setheading(270)
	goto(x - (bottom_len/4),y+(non_circle_len))
	fillcolor('#A01005')
	begin_fill()
	forward(non_circle_len - bottom_band_height)
	left(90)
	forward(bottom_len/2)
	left(90)
	forward(non_circle_len - bottom_band_height)
	end_fill()
	# goto(x+(bottom_r2)-(bottom_len/2),y+(non_circle_len - bottom_one_height))
	setheading(0)
	goto(x - (bottom_len/2),y+(non_circle_len)+len_square_bottom)
	right(90)
	# draw the shape with two circles on the two sides
	fillcolor('#F53F10')
	begin_fill()
	forward(bottom_one_height - bottom_r2+len_square_bottom)
	circle(bottom_r2,180)
	forward(bottom_one_height - bottom_r2+len_square_bottom)
	tmp_cir_x1,tmp_cir_y1 = pos()
	end_fill()
	#right side
	setheading(270)
	goto(x + (bottom_len/2),y+(non_circle_len)+len_square_bottom)
	begin_fill()
	forward(bottom_one_height - bottom_r2+len_square_bottom)
	circle(-bottom_r2,180)
	forward(bottom_one_height - bottom_r2+len_square_bottom)
	tmp_cir_x2,tmp_cir_y2 = pos()
	end_fill()
	# decoration, left side
	setheading(0)
	goto(x - (bottom_len/2) + (width * 0.02),y+(non_circle_len)+len_square_bottom)
	right(90)
	# draw the shape with two circles on the two sides
	fillcolor('#D7140E')
	begin_fill()
	forward(bottom_one_height - bottom_r2+len_square_bottom - (width * 0.01))
	circle(bottom_r2 - (width * 0.02),90)
	tmp_x1,tmp_y1 = pos() 
	circle(bottom_r2 - (width * 0.02),90)
	forward(bottom_one_height - bottom_r2+len_square_bottom - (width * 0.01))
	end_fill()
	setheading(0)
	goto(tmp_x1,tmp_y1+width * 0.03/2)
	val_for_cir = tmp_cir_x1 - (x - (bottom_len/2) + (width * 0.02)) - width * 0.03
	fillcolor('#FE9102')
	begin_fill()
	circle(val_for_cir/2)
	end_fill()
	goto(tmp_x1,tmp_y1+width * 0.03)
	setheading(0)
	num_peaces = 20
	for _ in range(num_peaces):
		circle(val_for_cir/2- width * 0.03/2,360/num_peaces/2)
		dot(width*0.012,'#F83201')
		circle(val_for_cir/2- width * 0.03/2,360/num_peaces/2)
	goto(tmp_x1,tmp_y1+width * 0.105)
	setheading(0)
	fillcolor('#7C0808')
	begin_fill()
	circle(val_for_cir/2- width * 0.09)
	end_fill()

	# decoration, right side
	setheading(0)
	goto(x + (bottom_len/2) - (width * 0.02),y+(non_circle_len)+len_square_bottom)
	right(90)
	# draw the shape with two circles on the two sides
	fillcolor('#D7140E')
	begin_fill()
	forward(bottom_one_height - bottom_r2+len_square_bottom - (width * 0.01))
	circle(-(bottom_r2 - (width * 0.02)),90)
	tmp_x1,tmp_y1 = pos() 
	circle(-(bottom_r2 - (width * 0.02)),90)
	forward(bottom_one_height - bottom_r2+len_square_bottom - (width * 0.01))
	end_fill()
	setheading(0)
	goto(tmp_x1,tmp_y1+width * 0.03/2)
	val_for_cir = tmp_cir_x1 - (x - (bottom_len/2) + (width * 0.02)) - width * 0.03
	fillcolor('#FE9102')
	begin_fill()
	circle(val_for_cir/2)
	end_fill()
	goto(tmp_x1,tmp_y1+width * 0.03)
	setheading(0)
	num_peaces = 20
	for _ in range(num_peaces):
		circle(val_for_cir/2- width * 0.03/2,360/num_peaces/2)
		dot(width*0.012,'#F83201')
		circle(val_for_cir/2- width * 0.03/2,360/num_peaces/2)
	goto(tmp_x1,tmp_y1+width * 0.105)
	setheading(0)
	fillcolor('#7C0808')
	begin_fill()
	circle(val_for_cir/2- width * 0.09)
	end_fill()

	draw_square(x,y+(non_circle_len)+(len_square_bottom/2),bottom_len,len_square_bottom/2,fill=True,border=0,clr='#9B9698')
	draw_square(x,y+(non_circle_len)+(len_square_bottom/2)+(width*0.01),bottom_len-(width*0.036*1),len_square_bottom/2-(width*0.01),fill=True,border=0,clr='#A6AAAB')
	draw_square(x,y+(non_circle_len)+(len_square_bottom/2)+(width*0.01*2),bottom_len-(width*0.036*2),len_square_bottom/2-(width*0.01*2),fill=True,border=0,clr='#B5B7B9')
	draw_square(x,y+(non_circle_len)+(len_square_bottom/2)+(width*0.01*3),bottom_len-(width*0.036*3),len_square_bottom/2-(width*0.01*3),fill=True,border=0,clr='#EDEDEF')

	# Draw the shape at the bottom, which look like a thaadi
	r = bottom_len / 2#((width**0.1)**2+(width*0.175)**2)/(2*(width*0.1)) + 5
	penup()
	setheading(0)
	goto(x,y)
	# draw the shape
	fillcolor('#7C0808')
	right(180)
	circle(-r,bottom_band_ang/2)
	begin_fill()
	right(180)
	circle(r,bottom_band_ang)
	tmp_x2, tmp_y2 = pos()
	cur_head = heading()
	setheading(90)
	forward(bottom_band_height)
	setheading(cur_head+180)
	tmp_x1,tmp_y1 = pos()
	chead = heading()
	circle(-r,bottom_band_ang)
	setheading(270)
	forward(bottom_band_height)
	end_fill()
	#decorations
	goto(tmp_x1,tmp_y1-(width * 0.02))
	setheading(chead)
	num_peaces = 28
	for _ in range(num_peaces-1):
		circle(-r,bottom_band_ang/num_peaces)
		dot(width * 0.01,'#fff')
	goto(tmp_x2,tmp_y2+(width * 0.02))
	setheading(chead)
	for _ in range(num_peaces-1):
		circle(-r,bottom_band_ang/num_peaces)
		dot(width * 0.01,'#fff')
	goto(tmp_x2,tmp_y2+(bottom_band_height/2))
	setheading(chead)
	num_peaces = 8
	for _ in range(num_peaces-1):
		circle(-r,bottom_band_ang/num_peaces)
		cx,cy = pos()
		chead = heading()
		draw_dashed_circle(cx,cy,width*0.02,'#FF5C01',20)
		goto(cx,cy)
		setheading(chead)
	# draw the head of theyyam
	setheading(0)
	draw_theyyam_face(x,y+bottom_band_height,width * 0.455)
	return height
	
def reset_position(x=0,y=0):
   setheading(0)
   goto(x,y)

def draw_squash(rad,num_rows,len_row,num_peaces,colors):
  # circle (rad)
  left(90)
  penup()
  initial = rad - (num_rows*len_row)
  forward(rad - initial)
  right(90)
  pendown()
  ang = 360 / num_peaces
  counter = 0
  right(90)
  for j in range(0,num_rows):
    # cur_peaces = int(2*(20+(10*j))*math.pi / prev_peace_length)
    for i in range(0,num_peaces):
        penup()
        fillcolor(colors[counter % len(colors)])
        begin_fill()
        left(90)
        circle(initial+(len_row*j),ang)
        right(90)
        forward(len_row)
        right(90)
        circle(-(initial+len_row+(len_row*j)),ang)
        right(90)
        forward(len_row)
        right(90)
        circle(initial+(len_row*j),ang)
        right(90)
        end_fill()
        counter += 1
    forward(len_row)
  return rad - initial

def draw_circular(rad,rad_len,sub_circle_count=3,colors=['red','green','blue'],num_peaces = 20,pen_down = True):
  x,y = pos()
  penup()
  vis_len = rad_len * 1
  second_rad_diff = rad_len / sub_circle_count
  ruler_circle_rad = rad - rad_len * 2
  ruler_ang = 360 / num_peaces
  circle(rad)
  for j in range(0,int(num_peaces)):
    # circle(rad_len)
    for i in range(0,sub_circle_count):
      # Draw the circles normally
      left(90)
      forward((second_rad_diff if i != 0 else 0 ))
      right(90)
      fillcolor(colors[i % len(colors)])
      begin_fill()
      if pen_down:pendown()
      circle(rad_len - (second_rad_diff * i))
      penup()
      end_fill()
    right(90)
    forward(rad_len-second_rad_diff)
    left(90)
    circle(rad,ruler_ang) # change the angle of circle
  # reset to normal position
  reset_position(x,y)
  left(180)
  # redraw the overflowing part at the end
  fillcolor(colors[0])
  begin_fill()
  if pen_down:pendown()
  circle(-rad_len,180) # first round
  right(90)
  penup()
  forward(second_rad_diff)
  right(90)
  if pen_down:pendown()
  circle((rad_len - second_rad_diff),180) # first round
  end_fill()
  left(90)
  penup()
  forward(second_rad_diff)
  left(90)
  fillcolor(colors[1])
  begin_fill()
  if pen_down:pendown()
  circle(-(rad_len - (second_rad_diff * 2)),180) # second round
  left(90)
  penup()
  forward(second_rad_diff)
  left(90)
  if pen_down:pendown()
  circle(rad_len-second_rad_diff,180) # second round
  end_fill()
  left(90)
  penup()
  forward(second_rad_diff)
  left(90)
  fillcolor(colors[2])
  begin_fill()
  if pen_down:pendown()
  circle(-(rad_len - (second_rad_diff * 2)),180) # third half round
  end_fill()
  penup()
  reset_position(x,y)
  circle(rad,ruler_ang) # redraw the second circle overflowed part
  left(180)
  fillcolor(colors[0])
  begin_fill()
  if pen_down:pendown()
  circle(-rad_len,180) # first round, second
  right(90)
  penup()
  forward(second_rad_diff)
  right(90)
  if pen_down:pendown()
  circle(rad_len - second_rad_diff,180) # first round, second 
  end_fill()
  penup()
  reset_position(x,y+rad_len)
  fillcolor('#2A3B1A')
  begin_fill()
  circle(rad-vis_len)
  end_fill()
  return vis_len


###############################
''' Radius of the pookalam '''# Change it 
rad = 450 # Circle all total  #	As you need
###############################


setup(1000,1000)
title("Pookalam by zoxilsi")
tracer(0,0) # Tracer is disabled for getting output instantly (remove if needed)
colormode(255)
bgcolor(30, 30, 30)
# Gentle golden gradient backdrop
draw_gradient_background((255, 215, 0), (255, 170, 0), 480)
update()
# speed(0) # Drawing speed maximum

penup() 
reset_position(0,-rad)
x,y = pos()
# draw squash
num_rows = 10 # Number of rows in the squash
len_row = 10 # height of a row in the squash
num_peaces = 40 # the number of peaces in which the circle want to be divided
colors = ["#536F3D","#5B0B16","#D6325C","#F06D0A",'#FACA27','#EDE9DE'] # the colors of the boxes in squash
# occ_squash = draw_squash(rad,num_rows,len_row,num_peaces,colors) # Draw the squash, it will return how much radius of total radius it 

# draw circular
circular_width = 40
cut_threshold = 1.3

colors2 = ['#9B232E','#BB5C08','#DEC727','#CCCDB4']
# occ_circular = draw_circular(new_rad,circular_width,colors=colors2,num_peaces=int(((new_rad)*math.pi*2)/(circular_width*cut_threshold)),sub_circle_count=4,pen_down=False) # draw circular shape 

occ_circular = draw_circular(rad,circular_width,colors=colors2,num_peaces=int(((rad)*math.pi*2)/(circular_width*cut_threshold)),sub_circle_count=5,pen_down=False) # draw circular shape 
reset_position(0,y=y+occ_circular) # reset the position to the occupied position before
# a background for the next draw_circular
padding_circle = 5
fillcolor('#2A3B1A')
begin_fill()
circle(rad-occ_circular)
end_fill()
new_rad = rad-occ_circular - padding_circle # the new radius for next shape
reset_position(y=y+occ_circular+padding_circle) # reset position to the next occupied position
occ_squash = draw_squash(new_rad,num_rows,len_row,num_peaces,colors) # Draw the squash, it will return how much radius of total radius it 

reset_position(0,y+occ_squash+padding_circle+occ_circular+5)
fillcolor('#D5D1AD')
begin_fill()
circle(rad - occ_squash-padding_circle-occ_circular-5)
end_fill()

draw_dashed_circle(0,0,rad - occ_squash-padding_circle-occ_circular-5,fillclr='#f2eecd',peaces=20)

# Geometric layers inside the inner cream ring (drawn beneath the Theyyam)
# Compute the effective inner radius of the cream ring
inner_R = rad - occ_squash - padding_circle - occ_circular - 5

# Outer bead ring near the cream boundary
draw_ring_beads(0, 0, inner_R * 0.95, count=72, size=6, clr='#9A4224')

# Lotus rosette centered within the ring
draw_lotus(0, 0, petal_count=24, inner_r=inner_R * 0.40, outer_r=inner_R * 0.25,
		   fill_main='#FF7A1A', fill_shadow='#D94E00')

# Inner Lotus (nested)
draw_lotus(0, 0, petal_count=12, inner_r=inner_R * 0.20, outer_r=inner_R * 0.12,
           fill_main='#FACA27', fill_shadow='#F06D0A')

# Mid bead ring to add rhythm
draw_ring_beads(0, 0, inner_R * 0.65, count=60, size=5, clr='#F2E6C7')

# Inner bead ring
draw_ring_beads(0, 0, inner_R * 0.1, count=24, size=4, clr='#9A4224')

th_height = draw_theyyam(0,rad*0.1,(rad-occ_squash-padding_circle-occ_circular-20)*2)

goto(0,0 - th_height/2 - ((rad-occ_squash-padding_circle-occ_circular-20)- th_height/2) / 2)
write("RITU '25",align="center",font=("Courier", int(rad*0.08), "bold"))
# placeholder (name)
width,height = screensize()
penup()
goto(width - 20,-rad+15)
setheading(270)
color('white')
pendown()
write("- zoxilsi",align="right",font=("Arial", 7, "normal"))
penup()
forward(15)
color('white')
pendown()
write("\"Pookalam\"",align="right",font=("Arial", 8, "bold"))
penup()

mainloop() # main loooooop

# Thank you !
