"""deleted added

Revision ID: d575f55ecc43
Revises: 7b3986e12694
Create Date: 2022-11-04 14:33:21.061041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd575f55ecc43'
down_revision = '7b3986e12694'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'actions', 'changes', ['action_description'], ['id'], ondelete='CASCADE')
    op.drop_column('actions', 'description')
    op.drop_column('actions', 'desc')
    op.add_column('tasks', sa.Column('is_deleted', sa.Boolean(), server_default='t', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'is_deleted')
    op.add_column('actions', sa.Column('desc', sa.INTEGER(), nullable=True))
    op.add_column('actions', sa.Column('description', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'actions', type_='foreignkey')
    # ### end Alembic commands ###