"""added is_delete field

Revision ID: b1425ce9a388
Revises: c63b3632c548
Create Date: 2022-11-04 11:09:15.003796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1425ce9a388'
down_revision = 'c63b3632c548'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'actions', 'changes', ['action_description'], ['id'], ondelete='CASCADE')
    op.drop_column('actions', 'description')
    op.drop_column('actions', 'desc')
    op.add_column('tasks', sa.Column('is_delete', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'is_delete')
    op.add_column('actions', sa.Column('desc', sa.INTEGER(), nullable=True))
    op.add_column('actions', sa.Column('description', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'actions', type_='foreignkey')
    # ### end Alembic commands ###
