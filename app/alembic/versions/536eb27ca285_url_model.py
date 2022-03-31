"""url_model

Revision ID: 536eb27ca285
Revises: 
Create Date: 2022-03-31 01:11:19.964300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '536eb27ca285'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('shortener',
    sa.Column('id', sa.INTEGER(), nullable=False, autoincrement=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('original_url', sa.String(255), nullable=False),
    sa.Column('short_uuid', sa.String(length=10), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_shortener')),
    sa.UniqueConstraint('id', name=op.f('uq_shortener_id'))
    )

    op.create_table('shortener_logs',
    sa.Column('id', sa.INTEGER(), nullable=False, autoincrement=True),
    sa.Column('shortener_id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_shortener_logs')),
    sa.UniqueConstraint('id', name=op.f('uq_shortener_logs_id')),
    sa.ForeignKeyConstraint(['shortener_id'], ['shortener.id'], name=op.f('fk_shortener_logs_shortener_id_shortener')),
    )

def downgrade():
    op.drop_table('shortener')
    op.drop_table('shortener_logs')
