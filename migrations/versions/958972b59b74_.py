"""empty message

Revision ID: 958972b59b74
Revises: 
Create Date: 2022-08-15 21:59:44.850248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '958972b59b74'
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
    sa.Column('role_user', sa.String(length=30), nullable=True),
    sa.Column('genero', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('aluno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('professor')
    op.drop_table('aluno')
    op.drop_table('user')
    # ### end Alembic commands ###