from manim import *

class QuadraticProof(Scene):
    def construct(self):
        # Proof of the Quadratic Formula
        intro = Text("Proof of the Quadratic Formula").scale(1.2).set_color(YELLOW)
        self.play(Write(intro), run_time=1)
        self.wait(1)
        self.play(FadeOut(intro), run_time=1)

        # Displaying the initial quadratic equation ax^2 + bx + c = 0
        equation = MathTex("ax^2 + bx + c = 0").scale(1.5)
        self.play(Write(equation))
        self.wait(0.5)

        # Multiplying by 4a
        equation_mult_4a = MathTex("4a^2x^2 + 4abx + 4ac = 0").scale(1.5)
        self.play(TransformMatchingShapes(equation, equation_mult_4a))
        self.wait(0.5)

        # Factoring as a perfect square
        equation_factored = MathTex("(2ax)^2 + 4abx + b^2 - b^2 + 4ac = 0").scale(1.5)
        underline = Underline(equation_factored[0][0:13], buff=0, color=YELLOW)
        down_arrow = Arrow(2 * LEFT, 2 * DOWN, color=YELLOW)
        down_arrow.next_to(underline.get_center(), DOWN, buff=0.4)
        self.play(TransformMatchingShapes(equation_mult_4a, equation_factored),
                  Create(underline),
                  Create(down_arrow))
        self.wait(0.5)

        # Adding text below the arrow
        text_below_arrow = MathTex("(2ax + b)^2").scale(1.5).next_to(down_arrow, DOWN, aligned_edge=LEFT)
        self.play(Write(text_below_arrow))
        self.wait(0.5)

        # Fading out elements quickly
        self.play(FadeOut(underline),
                  FadeOut(down_arrow),
                  FadeOut(text_below_arrow),
                  run_time=0.3)  # Adjusted time for faster fade-out
        self.wait(0.3)  # Reduced wait time

        # Simplifying the equation
        equation_simplified = MathTex("(2ax + b)^2 = b^2 - 4ac").scale(1.5)
        self.play(TransformMatchingShapes(equation_factored, equation_simplified))
        self.wait(0.5)

        # Taking square roots
        equation_sqrt = MathTex("2ax + b = \pm \sqrt{b^2 - 4ac}").scale(1.5)
        self.play(TransformMatchingShapes(equation_simplified, equation_sqrt))
        self.wait(0.5)

        # Isolating x
        equation_isolated_x = MathTex("2ax = -b \pm \sqrt{b^2 - 4ac}").scale(1.5)
        self.play(TransformMatchingShapes(equation_sqrt, equation_isolated_x))
        self.wait(0.5)

        # Final quadratic formula
        final_formula = MathTex("x = \\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(1.5)
        self.play(TransformMatchingShapes(equation_isolated_x, final_formula))
        self.wait(1)

        # Adding "Edited by: Arya" below the "Wrote by" text
        edited_by = Text("Edited by: Arya")
        self.play(FadeIn(edited_by))

        self.wait(2)
