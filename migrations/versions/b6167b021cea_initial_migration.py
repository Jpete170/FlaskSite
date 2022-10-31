"""Initial migration.

Revision ID: b6167b021cea
Revises: 
Create Date: 2022-10-31 15:43:08.153251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6167b021cea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=100), nullable=True),
    sa.Column('Birthdate', sa.String(length=100), nullable=True),
    sa.Column('Deathdate', sa.String(length=100), nullable=True),
    sa.Column('Bio', sa.String(length=500), nullable=True),
    sa.Column('IMG', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Author_Bio'), 'Author', ['Bio'], unique=False)
    op.create_index(op.f('ix_Author_Birthdate'), 'Author', ['Birthdate'], unique=False)
    op.create_index(op.f('ix_Author_Deathdate'), 'Author', ['Deathdate'], unique=False)
    op.create_index(op.f('ix_Author_IMG'), 'Author', ['IMG'], unique=False)
    op.create_index(op.f('ix_Author_Name'), 'Author', ['Name'], unique=False)
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('Year_Published', sa.Integer(), nullable=True),
    sa.Column('Author', sa.String(length=100), nullable=True),
    sa.Column('Description', sa.String(length=250), nullable=True),
    sa.Column('Genre', sa.String(length=100), nullable=True),
    sa.Column('Sub_Genre', sa.String(length=100), nullable=True),
    sa.Column('bookURL', sa.String(length=100), nullable=True),
    sa.Column('bookIMG', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_Author'), 'books', ['Author'], unique=False)
    op.create_index(op.f('ix_books_Description'), 'books', ['Description'], unique=False)
    op.create_index(op.f('ix_books_Genre'), 'books', ['Genre'], unique=False)
    op.create_index(op.f('ix_books_Sub_Genre'), 'books', ['Sub_Genre'], unique=False)
    op.create_index(op.f('ix_books_Year_Published'), 'books', ['Year_Published'], unique=False)
    op.create_index(op.f('ix_books_bookIMG'), 'books', ['bookIMG'], unique=False)
    op.create_index(op.f('ix_books_bookURL'), 'books', ['bookURL'], unique=False)
    op.create_index(op.f('ix_books_title'), 'books', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_books_title'), table_name='books')
    op.drop_index(op.f('ix_books_bookURL'), table_name='books')
    op.drop_index(op.f('ix_books_bookIMG'), table_name='books')
    op.drop_index(op.f('ix_books_Year_Published'), table_name='books')
    op.drop_index(op.f('ix_books_Sub_Genre'), table_name='books')
    op.drop_index(op.f('ix_books_Genre'), table_name='books')
    op.drop_index(op.f('ix_books_Description'), table_name='books')
    op.drop_index(op.f('ix_books_Author'), table_name='books')
    op.drop_table('books')
    op.drop_index(op.f('ix_Author_Name'), table_name='Author')
    op.drop_index(op.f('ix_Author_IMG'), table_name='Author')
    op.drop_index(op.f('ix_Author_Deathdate'), table_name='Author')
    op.drop_index(op.f('ix_Author_Birthdate'), table_name='Author')
    op.drop_index(op.f('ix_Author_Bio'), table_name='Author')
    op.drop_table('Author')
    # ### end Alembic commands ###
