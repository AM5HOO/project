from manim import *

class WriteStuff(Scene):
    def construct(self):
        name = Text("I want to share my favourite equations!")
        name.scale(0.75)  
        self.play(Write(name), run_time=3)
        self.wait()

        self.play(FadeOut(name))
        self.wait()

        first_line = Text("My first equation is: How to prove")
        second_line = MathTex("1N = 10^5 \\, \\text{dynes}")
        second_line.next_to(first_line, DOWN)
        self.play(Write(first_line))
        self.play(Write(second_line))
        self.wait(1)
        
        self.play(FadeOut(first_line), FadeOut(second_line))
        self.wait(1)

        example_tex_1 = MathTex("F = ma").scale(1)
        example_tex_2 = MathTex("\\Rightarrow N = 1 \\, \\text{kg} \\times 1 \\, \\text{m/s}^{2}").scale(1)
        example_tex_3 = MathTex("\\Rightarrow N = 1000 \\, \\text{g} \\times 100 \\, \\text{cm/s}^{2}").scale(1)
        example_tex_4 = MathTex("\\Rightarrow N = 10^5 \\, \\text{g} \\, \\text{cm/s}^{2}").scale(1)
        example_tex_5 = MathTex("\\Rightarrow 1N = 10^5 \\, \\text{dynes}", "(\\text{proved})").scale(1)

        example_tex_group = VGroup(example_tex_1, example_tex_2, example_tex_3, example_tex_4, example_tex_5)
        example_tex_group.arrange(DOWN)
        example_tex_group.width = config.frame_width - 2 * LARGE_BUFF

        self.play(Write(example_tex_1))
        self.wait(1)

        self.play(Write(example_tex_2))
        self.wait(2)

        self.play(TransformFromCopy(example_tex_2, example_tex_3), run_time=3)
        self.wait(2)

        self.play(TransformFromCopy(example_tex_3, example_tex_4), run_time=2)
        self.wait(2)

        self.play(Write(example_tex_5))
        self.wait(3)

        self.play(FadeOut(example_tex_group))
        self.wait(1)

        as_you_know_text = Text("As you know,")
        self.play(Write(as_you_know_text))
        self.wait(1)

        equation_text = MathTex("g \\, \\text{cm/s}^2 \\, \\text{or} \\, \\text{gcms}^{-2}", "\\, \\text{is regarded as dyne.}")
        equation_text.next_to(as_you_know_text, DOWN)
        self.play(Write(equation_text))
        self.wait(1)

        equation_text_2 = MathTex("kg \\, \\text{m/s}^2 \\, \\text{or} \\, \\text{kgms}^{-2}", "\\, \\text{is for Newton.}")
        equation_text_2.next_to(equation_text, DOWN)
        self.play(Write(equation_text_2))
        self.wait(2)

        self.play(FadeOut(VGroup(as_you_know_text, equation_text, equation_text_2)))

        and_text = Text("And lastly,")
        self.play(Write(and_text))
        self.wait(1)

        self.play(FadeOut(and_text))
        self.wait(1)

        equation = MathTex("F = G \\cdot \\frac{m_1 \\cdot m_2}{r^2}").scale(1)
        last_line = Text("Law of gravity").scale(0.7)
        last_line.next_to(equation, DOWN)
        self.play(Write(equation))
        self.play(Write(last_line))
        self.wait(1)

        self.play(FadeOut(equation, last_line))
        self.wait(1)

        outro = Text("Thank you")
        self.play(Write(outro))
        self.wait(1)

        self.play(FadeOut(outro))
        self.wait(1)
