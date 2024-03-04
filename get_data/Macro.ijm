open("D:/Computer_science/BE_PROJECT/Seed_Project/seedTestImage.jpeg");
//setTool("line");
makeLine(1230, 172, 1230, 216);
run("Set Scale...", "distance=44 known=10 unit=mm");
setOption("BlackBackground", true);
run("Convert to Mask");
run("Options...", "iterations=1 count=1 black do=[Fill Holes]");
run("Analyze Particles...", "size=70-Infinity show=Outlines display exclude overlay composite");
saveAs("Results", "D:/Computer_science/BE_PROJECT/Seed_Project/get_data/excelData/Results.csv");
selectWindow("Drawing of seedTestImage.jpeg");
saveAs("Jpeg", "D:/Computer_science/BE_PROJECT/Seed_Project/get_data/imageData/outline.jpg");
close();
selectWindow("seedTestImage.jpeg");
close();
close ("*")
if (isOpen ("Results")) { selectWindow ("Results"); run ("Close"); }
run("Quit");
