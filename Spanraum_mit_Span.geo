// Gmsh project created on Mon Jul 12 11:25:42 2021
SetFactory("OpenCASCADE");

prog = 1;//Progression
s = 0.1;// Mesh Size
trans = 20;// Transfinite 
basis = 10;

x = -((0.0094/2)*1000);
y = -((0.00514938/2)*1000);

Point(0) = {0 ,0 ,0 ,1.0};
//+
Point(1) = {9.4+x, 0+y, 0, 1.0};
//+
Point(2) = {0+x, 0.2+y, 0, 1.0};
//+
Point(3) = {0.58+x, 2+y, 0, 1.0};
//+
Point(4) = {0.58+x, 3.17+y, 0, 1.0};
//+
Point(5) = {6.1+x, 4.1+y, 0, 1.0};
//+
Point(6) = {9.1+x, 0+y, 0, 1.0};
//+
Point(19) = {0.2+x, 0+y, 0, 1.0};

//+
Line(3) = {3, 4};
//+
Point(7) = {8.95+x, 0.6+y, 0, 1.0};
//+

//+
Line(5) = {7, 5};
//+
Point(8) = {0.05+x, 1.4+y, 0, 1.0};
//+
Point(9) = {-0.2+x, 1.1+y, 0, 1.0};
//+
Point(10) = {-0.2+x, 0.7+y, 0, 1.0};

//+
Line(7) = {8, 3};
//+
Point(11) = {1.1+x, 4.1+y, 0, 1.0};
//+
Point(12) = {2.1+x, 4.8+y, 0, 1.0};
//+
Point(13) = {3.5+x, 5.1+y, 0, 1.0};
//+
Point(14) = {4.6+x, 5.1+y, 0, 1.0};
//+
Point(15) = {2+x, 0.2+y, 0, 1.0};
//+
Point(16) = {2+x, 2.2+y, 0, 1.0};

//+
Point(17) = {0.2+x, 0.2+y, 0, 1.0};
//+
Point(18) = {2+x, 2+y, 0, 1.0};
//+
Circle(10) = {17, 15, 18};

//+
Line(11) = {16, 18};
//+
Line(12) = {17, 19};
//+
Point(20) = {9+x, 0.2+y, 0, 1.0};
//+
Point(21) = {0.4+x, 0.2+y, 0, 1.0};
//+
Point(22) = {2.2+x, 1.8+y, 0, 1.0};
//+
Line(15) = {19, 21};
//+
Line(16) = {21, 20};
//+
Line(17) = {6, 20};
//+
Point(24) = {8.7+x, 0.6+y, 0, 1.0};
//+
Line(18) = {7, 24};
//+

//+
Line(21) = {18, 22};
//+
Point(25) = {6+x,3.9+y, 0, 1.0};
//+
Point(26) = {1.1+x, 3.9+y, 0, 1.0};
//+
Point(27) = {2.1+x, 4.6+y, 0, 1.0};
//+
Point(28) = {3.5+x, 4.9+y, 0, 1.0};
//+
Point(29) = {4.6+x, 4.9+y, 0, 1.0};
//+
Point(30) = {0.78+x, 3.07+y, 0, 1.0};
//+
Line(26) = {25, 24};
//+
Point(31) = {0.78+x, 2.04+y, 0, 1.0};
//+
Line(27) = {30, 31};
//+
Line(28) = {4, 30};
//+
Line(29) = {3, 31};
//+
Point(32) = {2.2+x, 2.4+y, 0, 1.0};
//+
Line(30) = {16, 32};
//+
Line(31) = {22, 32};
//+
Point(33) = {-0.08+x, 0.6+y, 0, 1.0};
//+
Line(33) = {22, 32};
//+
Point(34) = {-0.03+x, 1.09+y, 0, 1.0};
//+
Point(35) = {0.2+x, 1.4+y, 0, 1.0};
//+
Point(36) = {1.2+x, 2.3+y, 0, 1.0};
//+
Point(37) = {1.75+x, 2.4+y, 0, 1.0};
//+
BSpline(34) = {33, 34,35};
//+
Line(35) = {35, 31};
//+
BSpline(36) = {31, 36,37,32};
//+
Line(37) = {19, 6};
//+
Line(38) = {8, 35};
//+
Point(38) = {0.4+x, 0.4+y, 0, 1.0};
//+
Line(39) = {21, 38};
//+
Line(40) = {17, 38};

//+
Point(40) = {0.5+x, 0.9+y, 0, 1.0};
//+
Point(41) = {0.9+x, 1.4+y, 0, 1.0};
//+
Point(42) = {1.6+x, 1.8+y, 0, 1.0};
//+
BSpline(41) = {38, 40, 41, 42, 22};
//+

//+
Point(43) = {1.75+x, 2.2+y, 0, 1.0};
//+
Point(44) = {1.25+x, 2.1+y, 0, 1.0};
//+
Point(45) = {0.91+x, 1.91+y, 0, 1.0};
//+
Point(46) = {0.63+x, 1.73+y, 0, 1.0};
//+
Point(47) = {0.39+x, 1.41+y, 0, 1.0};
//+
Point(48) = {0.15+x, 1.15+y, 0, 1.0};
//+
Point(49) = {0.05+x, 0.83+y, 0, 1.0};

//+
BSpline(43) = {47, 46, 45};
//+
BSpline(44) = {45, 44, 43, 16};
//+
Line(45) = {47, 35};
//+
Line(46) = {45, 31};

//+
Point(50) = {-0.15+x, 0.5+y, 0, 1.0};
//+
Point(51) = {-0.1+x, 0.33+y, 0, 1.0};
//+
Point(52) = {-0+x, 0.52+y, 0, 1.0};
//+
Point(53) = {-0.01+x, 0.39+y, 0, 1.0};
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
Point(54) = {5.2+x, 5+y, 0, 1.0};
//+
Point(55) = {5.7+x, 4.6+y, 0, 1.0};
//+
BSpline(54) = {30, 26, 27, 28};
//+
Point(56) = {4.05+x, 5.2+y, 0, 1.0};
//+
Point(57) = {4.05+x, 5+y, 0, 1.0};
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
Point(58) = {5.2+x, 4.75+y, 0, 1.0};
//+
Point(59) = {5.7+x, 4.35+y, 0, 1.0};
//+
BSpline(60) = {29, 58, 59, 25};
//+
Line(61) = {5, 25};
//+
Point(60) = {9.25+x, 0.2+y, 0, 1.0};
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
Curve Loop(1) = {16, -17, -37, 15};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {39, -40, 12, 15};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {41, -21, -10, 40};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {11, 21, 31, -30};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {36, -30, -44, 46};
//+
Plane Surface(5) = {5};
//+
Curve Loop(6) = {43, 46, -35, -45};
//+
Plane Surface(6) = {6};
//+
Curve Loop(7) = {50, 45, -34, -48};
//+
Plane Surface(7) = {7};
//+
Curve Loop(8) = {52, 48, -47, -51};
//+
Plane Surface(8) = {8};
//+
Curve Loop(9) = {49, 38, -34, -47};
//+
Plane Surface(9) = {9};
//+
Curve Loop(10) = {35, -29, -7, 38};
//+
Plane Surface(10) = {10};
//+
Curve Loop(11) = {27, -29, 3, 28};
//+
Plane Surface(11) = {11};
//+
Curve Loop(12) = {54, -58, -53, 28};
//+
Plane Surface(12) = {12};
//+
Curve Loop(13) = {55, 59, -56, -58};
//+
Plane Surface(13) = {13};
//+
Curve Loop(14) = {60, -61, -57, 59};
//+
Plane Surface(14) = {14};
//+
Curve Loop(15) = {5, 61, 26, -18};
//+
Plane Surface(15) = {15};
//+
Curve Loop(16) = {62, -64, 65, 18};
//+
Plane Surface(16) = {16};
//+
Curve Loop(17) = {63, 17, -64, -66};
//+
Plane Surface(17) = {17};
//+
Curve Loop(18) = {26, 62, -16, 39, 41, 31, -36, -27, 54, 56, 60};
//+
Plane Surface(18) = {18};
//+

Extrude {0,0,1.25} {    
Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{9}; Surface{7}; Surface{8}; Surface{10}; Surface{11}; Surface{12};Surface{13}; Surface{14}; Surface{15}; Surface{16};Surface{17}; Surface{18}; Layers{11}; 
Recombine; 
}

//+
Transfinite Curve {17, 71, 15, 74, 40, 78, 21, 83, 30, 89, 46, 94, 45, 99, 48, 109, 112, 51, 66, 147} = 0.8*trans Using Progression prog;
//+
Transfinite Curve {63, 146, 64, 143} = trans Using Progression 1;
//+
Transfinite Curve {37, 73, 16, 69} = 10*basis Using Progression 1;
//+
Transfinite Curve {65, 65, 144, 62, 141} = 0.5*basis Using Progression 1;
//+
Transfinite Curve {5, 137, 26, 139} = 5*basis Using Progression 1;
//+
Transfinite Curve {135, 57, 132, 60} = 2*basis Using Progression 1;
//+
Transfinite Curve {56, 130, 55, 127} = 1.2*basis Using Progression 1;
//+
Transfinite Curve {54, 122, 53, 125} = 4*basis  Using Progression 1;
//+
Transfinite Curve {119, 3, 117, 27} = 1.3*basis Using Progression 1;
//+
Transfinite Curve {115, 7, 98, 98, 35, 96, 43} = 1*basis Using Progression 1;
//+
Transfinite Curve {49, 102, 105, 34, 108, 50} = 1*basis Using Progression 1;
//+
Transfinite Curve {93, 91} = 1.3*basis Using Progression 1;
//+
Transfinite Curve {44, 36} = 1.5*basis Using Progression 1;
//+
Transfinite Curve {11,86, 88, 31} = 1.2*trans Using Progression 1;
//+
Transfinite Curve {81, 41, 10, 84} = 2.5*basis Using Progression 1;
//+
Transfinite Curve {12, 39, 76, 79} = 0.3*basis Using Progression 1;
//+
Transfinite Curve {111, 52, 106, 47} = trans Using Progression 1;
//+
Transfinite Curve {38, 103, 114, 29, 28, 120, 58, 124, 59, 129, 129, 61, 134, 18, 140} = trans Using Progression 1;
//+



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
Transfinite Surface {12};
//+
Recombine Surface {12};

//+
Transfinite Surface {13};
//+
Recombine Surface {13};
//+
Transfinite Surface {14};
//+
Recombine Surface {14};
//+
Transfinite Surface {15};
//+
Recombine Surface {15};

//+
Transfinite Surface {16};
//+
Recombine Surface {16};
//+
Transfinite Surface {17};
//+
Recombine Surface {17};

//+
Recursive Delete {
  Curve{98}; 
}
//+
Recursive Delete {
  Curve{103}; 
}
//+
Recursive Delete {
  Curve{98}; 
}
//+
Recursive Delete {
  Curve{99}; 
}
//+
Recursive Delete {
  Curve{105}; 
}
//+
Recursive Delete {
  Curve{109}; 
}
//+
Recursive Delete {
  Curve{81}; 
}
//+
Recursive Delete {
  Curve{98}; 
}
//+
Recursive Delete {
  Curve{98}; 
}
//+
Recursive Delete {
  Curve{98}; 
}
//+
Recursive Delete {
  Curve{98}; 
}
//+
Recursive Delete {
  Curve{98}; 
}
//+
Recursive Delete {
  Curve{132}; 
}
//+
Recursive Delete {
  Curve{132}; 
}
//+
Recursive Delete {
  Curve{91}; 
}
r = 1/1.0001; // progression
n = 8; //number of layers
a = (r - 1) / (r^n - 1); 
one[0] = 1; 
layer[0] = a; 
For i In {1:n-1}    
one[i] = 1;   
layer[i] = layer[i-1] + a * r^i; 
EndFor
Extrude {0,0,0.15} {    
Surface{61}; Surface{65}; Surface{69}; Surface {85};Surface{43}; Surface{57}; Surface{48}; Surface{51}; Surface{54}; Surface{39}; Surface{35}; Surface{31};Surface{27};Surface{73};Surface{77};Surface{81};Surface{84};Surface{23};Recombine; 
Layers{one[], layer[]}; }


//+
Physical Surface("inlet") = {66};
//+
Physical Surface("outlet") = {80, 83};
//+
Physical Surface("wall") = {74, 72, 64, 59};
//+
Physical Surface("workpiece") = {21, 82,151, 147};
//+
Physical Surface("span") = {30, 26, 32, 37, 40, 49, 52};
//+
Physical Surface("tool") = {56, 44, 53};
//+
Physical Surface("back") = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18};
//+
Physical Surface("front") = {107, 94, 90, 98, 140, 143, 146, 150, 152, 134, 137, 90, 128, 131, 115, 112, 119,122, 125};
//+
Physical Surface("outlet_side_1") = {132, 135, 129};
//
Physical Surface("outlet_side_2") = {127, 108, 120, 123, 124, 116, 113 };
// 
Physical Surface("outlet_side_3") = {88};
// 
Physical Surface("outlet_side_4") = {93};
// 
Physical Surface("outlet_side_5") = {95};
// 
Physical Surface("outlet_side_6") = {139};
// 
Physical Surface("outlet_side_7") = {141};
// 
Physical Surface("outlet_side_8") = {145, 149};
// 
Physical Volume("spanraum") = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36};
// 
//+
Physical Surface("Surface") = {19, 62, 70, 75, 78, 101, 99, 106,100,97,91};
//
Physical Surface("Surface_verticale") = {58, 86};
//
Physical Surface("Surface_Span1") = {28, 103};
//
Physical Surface("Surface_Span2") = {41, 46, 36, 105, 110, 117};
//
Physical Surface("Surface_Span_verticale") = {33, 24, 104, 102};
