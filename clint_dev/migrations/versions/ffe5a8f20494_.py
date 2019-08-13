"""empty message

Revision ID: ffe5a8f20494
Revises: 6af130174709
Create Date: 2019-08-13 16:20:40.778649

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ffe5a8f20494'
down_revision = '6af130174709'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=50), nullable=False))
    op.add_column('user', sa.Column('password', sa.String(length=100), nullable=False))
    op.drop_index('u_account', table_name='user')
    op.drop_index('u_phone', table_name='user')
    op.create_unique_constraint(None, 'user', ['name'])
    op.drop_column('user', 'regist_time')
    op.drop_column('user', 'u_phone')
    op.drop_column('user', 'u_password')
    op.drop_column('user', 'u_level')
    op.drop_column('user', 'u_account')
    op.drop_column('user', 'u_name')
    op.drop_column('user', 'u_id')
    op.drop_column('user', 'u_statu')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('u_statu', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('u_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.add_column('user', sa.Column('u_name', mysql.VARCHAR(length=32), nullable=True))
    op.add_column('user', sa.Column('u_account', mysql.VARCHAR(length=32), nullable=True))
    op.add_column('user', sa.Column('u_level', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('u_password', mysql.VARCHAR(length=256), nullable=True))
    op.add_column('user', sa.Column('u_phone', mysql.VARCHAR(length=32), nullable=True))
    op.add_column('user', sa.Column('regist_time', sa.DATE(), nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('u_phone', 'user', ['u_phone'], unique=True)
    op.create_index('u_account', 'user', ['u_account'], unique=True)
    op.drop_column('user', 'password')
    op.drop_column('user', 'name')
    op.drop_column('user', 'id')
    # ### end Alembic commands ###
