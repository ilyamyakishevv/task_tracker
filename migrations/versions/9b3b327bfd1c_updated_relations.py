"""updated relations

Revision ID: 9b3b327bfd1c
Revises: 08bc6888b94b
Create Date: 2022-11-01 14:54:46.741188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b3b327bfd1c'
down_revision = '08bc6888b94b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actions', sa.Column('description', sa.Integer(), nullable=True))
    op.drop_index('ix_actions_desc', table_name='actions')
    op.create_index(op.f('ix_actions_description'), 'actions', ['description'], unique=False)
    op.create_foreign_key(None, 'actions', 'changes', ['description'], ['id'], ondelete='CASCADE')
    op.drop_column('actions', 'desc')
    op.drop_column('actions', 'action_description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actions', sa.Column('action_description', sa.INTEGER(), nullable=True))
    op.add_column('actions', sa.Column('desc', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'actions', type_='foreignkey')
    op.drop_index(op.f('ix_actions_description'), table_name='actions')
    op.create_index('ix_actions_desc', 'actions', ['desc'], unique=False)
    op.drop_column('actions', 'description')
    # ### end Alembic commands ###