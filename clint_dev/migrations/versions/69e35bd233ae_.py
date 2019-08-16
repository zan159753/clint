"""empty message

Revision ID: 69e35bd233ae
Revises: 
Create Date: 2019-08-16 10:07:49.836920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69e35bd233ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('advertising_orders',
    sa.Column('a_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=True),
    sa.Column('a_life_time', sa.Integer(), nullable=True),
    sa.Column('a_price', sa.Integer(), nullable=True),
    sa.Column('a_pay_statu', sa.Integer(), nullable=True),
    sa.Column('a_check_scheme_statu', sa.Integer(), nullable=True),
    sa.Column('a_apply_time', sa.Date(), nullable=True),
    sa.Column('a_pay_time', sa.Date(), nullable=True),
    sa.Column('s_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('a_id')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.String(length=32), nullable=False),
    sa.Column('loginName', sa.String(length=50), nullable=False),
    sa.Column('loginPwd', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('nature', sa.String(length=50), nullable=True),
    sa.Column('chId', sa.String(length=50), nullable=True),
    sa.Column('chKey', sa.String(length=50), nullable=True),
    sa.Column('salemanId', sa.String(length=32), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('loginName'),
    sa.UniqueConstraint('number'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('devices',
    sa.Column('d_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=True),
    sa.Column('d_code', sa.String(length=128), nullable=True),
    sa.Column('d_name', sa.String(length=32), nullable=True),
    sa.Column('d_sex', sa.Integer(), nullable=True),
    sa.Column('d_address', sa.String(length=32), nullable=True),
    sa.Column('d_type', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.Date(), nullable=True),
    sa.Column('end_time', sa.Date(), nullable=True),
    sa.Column('d_statu', sa.Integer(), nullable=True),
    sa.Column('d_scheme_size', sa.String(length=32), nullable=True),
    sa.Column('m_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('d_id'),
    sa.UniqueConstraint('d_code')
    )
    op.create_table('medias',
    sa.Column('m_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('m_name', sa.String(length=32), nullable=True),
    sa.Column('m_type', sa.Integer(), nullable=True),
    sa.Column('m_size', sa.String(length=32), nullable=True),
    sa.Column('m_format', sa.String(length=16), nullable=True),
    sa.Column('m_url', sa.String(length=256), nullable=True),
    sa.Column('m_memory', sa.String(length=32), nullable=True),
    sa.Column('u_id', sa.Integer(), nullable=True),
    sa.Column('t_id', sa.Integer(), nullable=True),
    sa.Column('m_upload_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('m_id')
    )
    op.create_table('themes',
    sa.Column('t_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('t_name', sa.String(length=32), nullable=True),
    sa.Column('u_id', sa.Integer(), nullable=True),
    sa.Column('t_url', sa.String(length=256), nullable=True),
    sa.Column('t_pic_loop', sa.Integer(), nullable=True),
    sa.Column('t_vedio_loop', sa.Integer(), nullable=True),
    sa.Column('t_type', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('t_id'),
    sa.UniqueConstraint('t_name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('device',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('clientNumber', sa.String(length=32), nullable=True),
    sa.Column('number', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('province', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('district', sa.String(length=50), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('latitude', sa.Integer(), nullable=True),
    sa.Column('longitude', sa.Integer(), nullable=True),
    sa.Column('state', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('mediacode', sa.String(length=50), nullable=True),
    sa.Column('salecity', sa.String(length=50), nullable=True),
    sa.Column('product_time', sa.DateTime(), nullable=True),
    sa.Column('carnum', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.Integer(), nullable=True),
    sa.Column('version', sa.String(length=50), nullable=True),
    sa.Column('updatefile', sa.String(length=128), nullable=True),
    sa.Column('spec', sa.String(length=50), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['clientNumber'], ['client.number'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number'),
    mysql_collate='utf8_general_ci'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('device')
    op.drop_table('user')
    op.drop_table('themes')
    op.drop_table('medias')
    op.drop_table('devices')
    op.drop_table('client')
    op.drop_table('advertising_orders')
    # ### end Alembic commands ###