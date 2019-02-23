from random import randint, choice


def sidewinder(grid):
    for row in grid.each_row():
        run = []
        for c in row:
            run.append(c)
            at_easter_boundary = c.east is None
            at_northern_boundary = c.north is None

            should_close_out = at_easter_boundary or (not at_northern_boundary and randint(0, 1) == 0)

            if should_close_out:
                member = choice(run)
                if member.north:
                    member.link(member.north)
                run = []
            else:
                c.link(c.east)
