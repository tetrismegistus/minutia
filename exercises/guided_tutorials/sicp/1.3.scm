;Define a procedure that takes three numbers as arguments
;and returns the sum of the squares of the two larger numbers

(define (square x) (* x x ))

(define (sum_of_squares x y)
  (+ (square x)
     (square y)))

(define (sum_of_largest_squares x y z)
  (cond ((and (> x y) (> y z)) (sum_of_squares x y))
	    ((and (> x y) (> z y)) (sum_of_squares x z))
	    ((and (> y x) (> z x)) (sum_of_squares y z))))

(sum_of_largest_squares 9 10 11)

