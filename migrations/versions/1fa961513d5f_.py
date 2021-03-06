"""empty message

Revision ID: 1fa961513d5f
Revises: faca79430a5d
Create Date: 2018-05-03 15:46:46.997243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fa961513d5f'
down_revision = 'faca79430a5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('bucketlists', sa.Column('created_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'bucketlists', 'users', ['created_by'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bucketlists', type_='foreignkey')
    op.drop_column('bucketlists', 'created_by')
    op.drop_table('users')
    # ### end Alembic commands ###
