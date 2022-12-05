"""empty message

Revision ID: f761fcef1bc9
Revises: 6b102e70702a
Create Date: 2022-12-04 21:05:17.148088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f761fcef1bc9'
down_revision = '6b102e70702a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.drop_constraint('team_pokemon_id_fkey', type_='foreignkey')
        batch_op.drop_column('pokemon_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pokemon_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('team_pokemon_id_fkey', 'pokemon', ['pokemon_id'], ['id'])

    # ### end Alembic commands ###