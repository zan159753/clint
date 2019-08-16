"""empty message

Revision ID: af6765d8ee21
Revises: 69e35bd233ae
Create Date: 2019-08-16 10:08:35.187859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af6765d8ee21'
down_revision = '69e35bd233ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medias_pag__schemes',
    sa.Column('p_t_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('p_id', sa.Integer(), nullable=True),
    sa.Column('t_id', sa.Integer(), nullable=True),
    sa.Column('p_t_week', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('p_t_id')
    )
    op.create_table('medias_pags',
    sa.Column('p_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('p_code', sa.String(length=64), nullable=True),
    sa.Column('p_type', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('p_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medias_pags')
    op.drop_table('medias_pag__schemes')
    # ### end Alembic commands ###
