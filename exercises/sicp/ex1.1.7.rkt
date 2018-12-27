(define (sqrt-iter guess x)
  (if (good-enough? guess x)
    guess
    (sqrt-iter (improve guess x)x)
    )
  )

(define (improve guess x)
  (average guess (/ x guess))
  )

(define (average x y)
  (/ (+ x y) 2)
  )

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.011)
  )

(define (square x) (* x x))

(define (sqrt x)
  (sqrt-iter 1.0 x)
  )

(sqrt 9)

(sqrt (+ 100 37))

(sqrt (+ (sqrt 2) (sqrt 3)))

(square (sqrt 1000))

