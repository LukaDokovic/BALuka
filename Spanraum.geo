// Gmsh project created on Mon Jul 12 11:25:42 2021
SetFactory("OpenCASCADE");

prog = 1.1;//Progression
s = 0.1;// Mesh Size
trans = 10;// Transfinite 
basis = 10;
// arc

x = -((0.0094/2)*1000);
y = -((0.00514938/2)*1000);

//+
Point(0) = {0 ,0 ,0 ,1.0};
//+
Point(1) = {9.4 + x, 0 + y, 0, 1.0};
//+
Point(2) = {0+ x, 0.2+ y, 0, 1.0};
//+
Point(3) = {0.58+ x, 2+ y, 0, 1.0};
//+
Point(4) = {0.58+ x, 3.17+ y, 0, 1.0};
//+
Point(5) = {6.1+ x, 4.1+ y, 0, 1.0};
//+
Point(6) = {9.1+ x, 0+ y, 0, 1.0};

//+
Line(3) = {3, 4};
//+
Point(7) = {8.95+ x, 0.6+ y, 0, 1.0};
//+

//+
Line(5) = {7, 5};
//+
Point(8) = {0.05+ x, 1.4+ y, 0, 1.0};
//+
Point(9) = {-0.2+ x, 1.1+ y, 0, 1.0};
//+
Point(10) = {-0.2+ x, 0.7+ y, 0, 1.0};

//+
Line(7) = {8, 3};
//+
Point(11) = {1.1+ x, 4.1+ y, 0, 1.0};
//+
Point(12) = {2.1+ x, 4.8+ y, 0, 1.0};
//+
Point(13) = {3.5+ x, 5.1+ y, 0, 1.0};
//+
Point(14) = {4.6+ x, 5.1+ y, 0, 1.0};
//+
//Point(15) = {2, 0.2, 0, 1.0};
//+
Point(16) = {2+ x, 2.2+ y, 0, 1.0};
//+
// Point(17) = {4, 0, 0, 1.0};
// +
// Point(18) = {4.2, 0, 0, 1.0};
//+
Point(20) = {9+ x, 0.2+ y, 0, 1.0};
//+
Line(8) = {2, 20};




//+
// Line(16) = {21, 20};
//+
Line(17) = {6, 20};
//+
Point(24) = {8.7+ x, 0.6+ y, 0, 1.0};
//+
Line(18) = {7, 24};
//+


//+
Point(25) = {6+ x,3.9+ y, 0, 1.0};
//+
Point(26) = {1.1+ x, 3.9+ y, 0, 1.0};
//+
Point(27) = {2.1+ x, 4.6+ y, 0, 1.0};
//+
Point(28) = {3.5+ x, 4.9+ y, 0, 1.0};
//+
Point(29) = {4.6+ x, 4.9+ y, 0, 1.0};
//+
Point(30) = {0.78+ x, 3.07+ y, 0, 1.0};
//+
Line(26) = {25, 24};
//+
Point(31) = {0.78+ x, 2.04+ y, 0, 1.0};
//+
Line(27) = {30, 31};
//+
Line(28) = {4, 30};
//+
Line(29) = {3, 31};
//+
Point(32) = {2+ x, 2.4+ y, 0, 1.0};
//+
Line(30) = {16, 32};

//+
Point(33) = {0.05+ x, 0.6+ y, 0, 1.0};

//+
Point(34) = {-0.03+ x, 1.09+ y, 0, 1.0};
//+
Point(35) = {0.25+ x, 1.4+ y, 0, 1.0};
//+
Point(36) = {1.2+ x, 2.3+ y, 0, 1.0};
//+
Point(37) = {1.75+ x, 2.4+ y, 0, 1.0};
//+
BSpline(34) = {33, 34,35};
//+
Line(35) = {35, 31};
//+
BSpline(36) = {31, 36,37,32};
//+

// Line(37) = {19, 6};


//+
Line(38) = {8, 35};


// Point(40) = {0.5, 0.9, 0, 1.0};
// +
// Point(41) = {0.9, 1.4, 0, 1.0};
// +
// Point(42) = {1.6, 1.8, 0, 1.0};
// +
// BSpline(41) = {38, 40, 41, 42, 22};
// +

//+
Point(43) = {1.75+ x, 2.2+ y, 0, 1.0};
//+
Point(44) = {1.25+ x, 2.1+ y, 0, 1.0};
//+
Point(45) = {0.91+ x, 1.91+ y, 0, 1.0};
//+
Point(46) = {0.63+ x, 1.73+ y, 0, 1.0};
//+
Point(47) = {0.39+ x, 1.41+ y, 0, 1.0};
//+
Point(48) = {0.15+ x, 1.15+ y, 0, 1.0};
//+
Point(49) = {0.05+ x, 0.83+ y, 0, 1.0};

//+
BSpline(43) = {47, 46, 45};
//+
BSpline(44) = {45, 44, 43, 16};
//+
Line(45) = {47, 35};

//+
Line(46) = {45, 31};

//+
Point(50) = {-0.15+ x, 0.5+ y, 0, 1.0};
//+
Point(51) = {-0.1+ x, 0.30+ y, 0, 1.0};
//+
Point(52) = {-0+ x, 0.52+ y, 0, 1.0};
//+
Point(53) = {-0.01+ x, 0.39+ y, 0, 1.0};
//+
Line(47) = {50,33};
//+
Line(48) = {52,33};
//+
BSpline(49) = {50, 10, 9, 8};
//+
BSpline(50) = {52, 49, 48, 47};
//+
BSpline(51) = {2, 51, 50};
//+
BSpline(52) = {2, 53, 52};
//+
//+
BSpline(53) = {4, 11, 12, 13};
//+
Point(54) = {5.2+ x, 5+ y, 0, 1.0};
//+
Point(55) = {5.7+ x, 4.6+ y, 0, 1.0};
//+
BSpline(54) = {30, 26, 27, 28};
//+
Point(56) = {4.05+ x, 5.2+ y, 0, 1.0};
//+
Point(57) = {4.05+ x, 5+ y, 0, 1.0};
//+
BSpline(55) = {13, 56, 14};
//+
BSpline(56) = {28, 57, 29};
//+
BSpline(57) = {14, 54, 55, 5};
//+
Line(58) = {13, 28};
//+
Line(59) = {14, 29};
//+
Point(58) = {5.2+ x, 4.75+ y, 0, 1.0};
//+
Point(59) = {5.7+ x, 4.35+ y, 0, 1.0};
//+
BSpline(60) = {29, 58, 59, 25};
//+
Line(61) = {5, 25};
//+
Point(60) = {9.25+ x, 0.2+ y, 0, 1.0};
//+
Line(62) = {24, 20};
//+
Line(63) = {1, 6};
//+
Line(64) = {60, 20};
//+
Line(65) = {60, 7};
//+
Line(66) = {1, 60};




//+
Recursive Delete {
  Curve{36}; 
}
//+
Recursive Delete {
  Curve{30}; 
}
//+
Recursive Delete {
  Curve{44}; 
}
//+
Recursive Delete {
  Point{43}; 
}
//+
Recursive Delete {
  Point{37}; 
}
//+
Recursive Delete {
  Point{36}; 
}
//+
Recursive Delete {
  Point{44}; 
}
//+
Recursive Delete {
  Curve{50}; 
}
//+
Recursive Delete {
  Curve{43}; 
}
//+
Recursive Delete {
  Point{46}; 
}
//+
Recursive Delete {
  Curve{45}; 
}
//+
Recursive Delete {
  Curve{38}; 
}
//+
Recursive Delete {
  Curve{46}; 
}
//+
Recursive Delete {
  Point{48}; 
}
//+
Recursive Delete {
  Point{49}; 
}
//+
Recursive Delete {
  Curve{48}; 
}
//+
Recursive Delete {
  Curve{52}; 
}
//+
Recursive Delete {
  Point{53}; 
}
//+
Line(67) = {8, 35};
//+
Recursive Delete {
  Curve{51}; 
}
//+
Point(61) = {0+ x, -0+ y, 0, 1.0};
//+
Recursive Delete {
  Curve{8}; 
}
//+
Line(68) = {61, 6};
//+
BSpline(69) = {50, 51, 61};
//+
Point(62) = {0.15+ x, 0.2+ y, 0, 1.0};
//+
Line(70) = {33, 62};
//+
Line(71) = {61, 62};
//+
Line(72) = {20, 62};
//+
Curve Loop(1) = {72, -71, 68, 17};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {70, -71, -69, 47};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {34, -67, -49, 47};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {29, -35, -67, 7};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {27, -29, 3, 28};
//+
Plane Surface(5) = {5};
//+
Curve Loop(6) = {54, -58, -53, 28};
//+
Plane Surface(6) = {6};
//+
Curve Loop(7) = {55, 59, -56, -58};
//+
Plane Surface(7) = {7};
//+
Curve Loop(8) = {60, -61, -57, 59};
//+
Plane Surface(8) = {8};
//+
Curve Loop(9) = {5, 61, 26, -18};
//+
Plane Surface(9) = {9};
//+
Curve Loop(10) = {62, -64, 65, 18};
//+
Plane Surface(10) = {10};
//+
Curve Loop(11) = {63, 17, -64, -66};
//+
Plane Surface(11) = {11};
//+
Curve Loop(12) = {26, 62, 72, -70, 34, 35, -27, 54, 56, 60};
//+
Plane Surface(12) = {12};

//+

Extrude {0,0,1.25} {    
Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{9}; Surface{7}; Surface{8}; Surface{10}; Surface{11}; Surface{12}; Layers{7}; Recombine; 
}

//+
Transfinite Curve {17, 80, 66, 127, 71, 77} = 1* trans Using Progression prog;
//+
Transfinite Curve {47, 85, 67, 89, 29, 93, 28, 100, 58, 104, 117, 117, 59, 61, 110, 18, 113, 64, 123, 63, 126} = 10 Using Progression 1;
//+
Transfinite Curve {79, 68, 72, 75} = 10*basis Using Progression 1;

Transfinite Curve {82, 84} = 1*basis Using Progression 1;
//+
Transfinite Curve {62, 121, 124, 65} = 0.5*basis Using Progression 1;
//+
Transfinite Curve {112, 26, 108, 5} = 5*basis  Using Progression 1;
//+
Transfinite Curve {57, 120, 119, 60} = 2*basis Using Progression 1;
//+
Transfinite Curve {54, 102} = 4*basis Using Progression 1;
//+
Transfinite Curve {53, 105} = 4*basis Using Progression 1;
//+
Transfinite Curve {97, 27, 3, 99} = 1.4*basis Using Progression 1;
//+
Transfinite Curve {56, 118, 55, 115} = 1*basis Using Progression 1;
//+
Transfinite Curve {35, 94, 7, 95} = 1*basis Using Progression 1;
//+
Transfinite Curve {34, 87, 49, 90} = 1*basis  Using Progression 1;
//+
Transfinite Curve {70, 69} = 0.5*basis Using Progression 1;


//+
Transfinite Surface {1};
//+
Recombine Surface {1};
//+
Transfinite Surface {2};
//+
Recombine Surface {2};

//+
Transfinite Surface {3};
//+
Recombine Surface {3};
//+
Transfinite Surface {4};
//+
Recombine Surface {4};

//+
Transfinite Surface {5};
//+
Recombine Surface {5};
//+
Transfinite Surface {6};
//+
Recombine Surface {6};

//+
Transfinite Surface {7};
//+
Recombine Surface {7};
//+
Transfinite Surface {8};
//+
Recombine Surface {8};

//+
Transfinite Surface {9};
//+
Recombine Surface {9};
//+
Transfinite Surface {10};
//+
Recombine Surface {10};

//+
Transfinite Surface {11};
//+
Recombine Surface {11};
//+ 

//+
r = 1/1.25; // progression
n = 6; //number of layers
a = (r - 1) / (r^n - 1); 
one[0] = 1; 
layer[0] = a; 
For i In {1:n-1}    
one[i] = 1;   
layer[i] = layer[i-1] + a * r^i; 
EndFor
Extrude {0,0,0.15} {    
Surface{17}; Surface{21}; Surface{25}; Surface{29}; Surface{33}; Surface{37}; Surface{46}; Surface{49}; Surface{42}; Surface{53}; Surface{56}; Surface{57};Recombine; 
Layers{one[], layer[]}; }

//+

Physical Surface("inlet") = {43};
//+
Physical Surface("outlet") = {52, 55};
//+
Physical Surface("wall") = {38, 48, 36, 31};
//+
Physical Surface("tool") = {28, 24, 19 };
//+
Physical Surface("workpiece") = {15, 54, 60, 99};
//+
Physical Surface("front") = {102, 62, 66, 70, 74, 78, 82, 86, 90 ,94, 98, 101};
//+
Physical Surface("back") = {1, 2, 3, 4, 5, 7, 6, 9, 8, 10, 11, 12};
//+
Physical Surface("outlet_side_1") = {64, 69};
//+
Physical Surface("outlet_side_2") = {73};
//+
Physical Surface("outlet_side_3") = {76};
//+
Physical Surface("outlet_side_4") = {81};
//+
Physical Surface("outlet_side_5") = {83};
//+
Physical Surface("outlet_side_6") = {89};
//+
Physical Surface("outlet_side_7") = {91};
//+
Physical Surface("outlet_side_8") = {97, 100};
//+
//Physical Surface("outlet_side") = {76, 81, 83, 89, 91, 97, 100, 64, 69, 73};
//+
Physical Surface("Surface") = {13, 58, 18, 63,22,67,27,72,34,79,47,87,40,92,50,95,85 };
//+
// Physical Surface("Surface_tool1") = {18,63};
// //+
// Physical Surface("Surface_tool2") = {22,67};
// //+
// Physical Surface("Surface_tool3") = {27,72};
// //+
Physical Surface("Surface_wall_left1") = {30,75};
// //+
// Physical Surface("Surface_wall_left2") = {34,79};
// //+
// Physical Surface("Surface_wall_right1") = {47,87};
// //+
// Physical Surface("Surface_wall_right2") = {40,92};
// //+
// Physical Surface("Surface_outlet") = {50,95};
// //+
// Physical Surface("Surface_inlet") = {45,85};
//+
Physical Volume("spanraum") = {1, 2, 3, 4, 5, 7, 6, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24};
//+
