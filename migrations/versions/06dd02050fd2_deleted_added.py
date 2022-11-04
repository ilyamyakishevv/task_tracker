"""deleted added

Revision ID: 06dd02050fd2
Revises: 811ebf7e28bd
Create Date: 2022-11-04 14:38:03.939781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06dd02050fd2'
down_revision = '811ebf7e28bd'
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
