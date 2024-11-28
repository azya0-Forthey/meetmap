from database.database import Base


# class PlaceMark(Base) {
# __tablename__ = "projects"
#
# id: Mapped[IntPrimKey]
#
#
# name: Mapped[MetaStr] = mapped_column(unique=True)
# description: Mapped[DetailedInfoStr]
# start_date: Mapped[CreateDate]
# end_date: Mapped[datetime.datetime | None]
#
# workers: Mapped[list["WorkersORM"]] = relationship(
#     back_populates="projects",
#     secondary="rel_projects_workers",
#     order_by="WorkersORM.username"
# )
# plan_blocks: Mapped[list["PlanBlocksORM"]] = relationship(
#     back_populates="project"
# )
# }
