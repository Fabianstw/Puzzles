mod d1;
mod d2;
mod d3;
mod d4;
mod d5;
mod d6;
mod d7;
mod d8;
mod d9;

fn main() {
  const DAY: i8 = 9;
  if DAY == 1 {
    d1::d1p1::solve();
    d1::d1p2::solve();
  } else if DAY == 2 {
    d2::d2p1::solve();
    d2::d2p2::solve();
  } else if DAY == 3 {
    d3::d3p1::solve();
    d3::d3p2::solve();
  } else if DAY == 4 {
    d4::d4p1::solve();
    d4::d4p2::solve();
  } else if DAY == 5 {
    d5::d5p1::solve();
    d5::d5p2::solve();
  } else if DAY == 6 {
    d6::d6p1::solve();
  } else if DAY == 7 {
    d7::d7p1::solve();
  } else if DAY == 8 {
    d8::d8p1::solve();
    d8::d8p2::solve();
  } else if DAY == 9 {
    d9::d9p1::solve();
    d9::d9p2::solve();
  }
}
