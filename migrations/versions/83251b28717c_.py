"""empty message

Revision ID: 83251b28717c
Revises: 
Create Date: 2022-08-11 18:03:19.193651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83251b28717c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.Column('senha_hash', sa.LargeBinary(length=128), nullable=True),
    sa.Column('data_nascimento', sa.String(length=20), nullable=True),
    sa.Column('genero', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###