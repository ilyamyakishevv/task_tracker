"""added action model

Revision ID: 432cb7303002
Revises: e0579fe9142e
Create Date: 2022-10-29 12:11:42.359774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '432cb7303002'
down_revision = 'e0579fe9142e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('object_name', sa.String(), nullable=False),
    sa.Column('object_id', sa.Integer(), nullable=False),
    sa.Column('action_user', sa.String(), nullable=False),
    sa.Column('action_description', sa.String(), nullable=False),
    sa.Column('action_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_action_action_description'), 'action', ['action_description'], unique=False)
    op.create_index(op.f('ix_action_action_user'), 'action', ['action_user'], unique=False)
    op.create_index(op.f('ix_action_object_id'), 'action', ['object_id'], unique=False)
    op.create_index(op.f('ix_action_object_name'), 'action', ['object_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_action_object_name'), table_name='action')
    op.drop_index(op.f('ix_action_object_id'), table_name='action')
    op.drop_index(op.f('ix_action_action_user'), table_name='action')
    op.drop_index(op.f('ix_action_action_description'), table_name='action')
    op.drop_table('action')
    # ### end Alembic commands ###