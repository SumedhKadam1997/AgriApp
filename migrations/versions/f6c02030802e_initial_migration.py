"""initial migration

Revision ID: f6c02030802e
Revises: 
Create Date: 2020-12-19 23:12:42.697847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6c02030802e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=124), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('contactform',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('subject', sa.String(length=124), nullable=True),
    sa.Column('message', sa.String(length=1024), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('crop_name', sa.String(length=64), nullable=False),
    sa.Column('date_planted', sa.DateTime(), nullable=True),
    sa.Column('area', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fretilizers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('crop_id', sa.Integer(), nullable=False),
    sa.Column('date_of_apply', sa.DateTime(), nullable=True),
    sa.Column('urea', sa.Integer(), nullable=True),
    sa.Column('dap', sa.Integer(), nullable=True),
    sa.Column('ammonium_sulphate', sa.Integer(), nullable=True),
    sa.Column('bag_of_12X32X16', sa.Integer(), nullable=True),
    sa.Column('bag_of_10X26X26', sa.Integer(), nullable=True),
    sa.Column('mop', sa.Integer(), nullable=True),
    sa.Column('micronutrients', sa.Integer(), nullable=True),
    sa.Column('sulphur', sa.Integer(), nullable=True),
    sa.Column('bag_of_19X19X19', sa.Integer(), nullable=True),
    sa.Column('bag_of_20X20X0X13', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['crop_id'], ['crops.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('watersolublefert',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('crop_id', sa.Integer(), nullable=False),
    sa.Column('date_of_apply', sa.DateTime(), nullable=True),
    sa.Column('bag_of_19X19X19', sa.Integer(), nullable=True),
    sa.Column('bag_of_13X40X13', sa.Integer(), nullable=True),
    sa.Column('bag_of_13X0X45', sa.Integer(), nullable=True),
    sa.Column('bag_of_0X52X34', sa.Integer(), nullable=True),
    sa.Column('bag_of_12X61X0', sa.Integer(), nullable=True),
    sa.Column('calcium_nitrate', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['crop_id'], ['crops.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('watersolublefert')
    op.drop_table('fretilizers')
    op.drop_table('crops')
    op.drop_table('contactform')
    op.drop_table('users')
    # ### end Alembic commands ###
