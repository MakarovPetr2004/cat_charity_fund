"""Foreign Key user_id added

Revision ID: 671f0a3a98fd
Revises: 10b647838e59
Create Date: 2024-02-17 15:43:07.476703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '671f0a3a98fd'
down_revision = '10b647838e59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_donation_user_id_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.drop_constraint('fk_donation_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
