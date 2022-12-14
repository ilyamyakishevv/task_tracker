"""deleted added

Revision ID: daeae569ecf6
Revises: 06dd02050fd2
Create Date: 2022-11-04 14:38:17.735906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daeae569ecf6'
down_revision = '06dd02050fd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'actions', 'changes', ['action_description'], ['id'], ondelete='CASCADE')
    op.drop_column('actions', 'desc')
    op.drop_column('actions', 'description')
    op.add_column('tasks', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'is_deleted')
    op.add_column('actions', sa.Column('description', sa.INTEGER(), nullable=True))
    op.add_column('actions', sa.Column('desc', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'actions', type_='foreignkey')
    # ### end Alembic commands ###
