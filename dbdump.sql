PGDMP                         x            parsedaccounts    12.3    12.3 ?    m           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            n           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            o           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            p           1262    16396    parsedaccounts    DATABASE     �   CREATE DATABASE parsedaccounts WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
    DROP DATABASE parsedaccounts;
                postgres    false            �            1259    16399 
   bannedbots    TABLE     �   CREATE TABLE public.bannedbots (
    id integer NOT NULL,
    telephone text NOT NULL,
    password text NOT NULL,
    bandate date NOT NULL
);
    DROP TABLE public.bannedbots;
       public         heap    postgres    false            q           0    0    TABLE bannedbots    COMMENT     /   COMMENT ON TABLE public.bannedbots IS 'TRIAL';
          public          postgres    false    203            r           0    0    COLUMN bannedbots.id    COMMENT     3   COMMENT ON COLUMN public.bannedbots.id IS 'TRIAL';
          public          postgres    false    203            s           0    0    COLUMN bannedbots.telephone    COMMENT     :   COMMENT ON COLUMN public.bannedbots.telephone IS 'TRIAL';
          public          postgres    false    203            t           0    0    COLUMN bannedbots.password    COMMENT     9   COMMENT ON COLUMN public.bannedbots.password IS 'TRIAL';
          public          postgres    false    203            u           0    0    COLUMN bannedbots.bandate    COMMENT     8   COMMENT ON COLUMN public.bannedbots.bandate IS 'TRIAL';
          public          postgres    false    203            �            1259    16397    bannedbots_id_seq    SEQUENCE     �   CREATE SEQUENCE public.bannedbots_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.bannedbots_id_seq;
       public          postgres    false    203            v           0    0    bannedbots_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.bannedbots_id_seq OWNED BY public.bannedbots.id;
          public          postgres    false    202            �            1259    16410    bots    TABLE     �   CREATE TABLE public.bots (
    id integer NOT NULL,
    telephone text NOT NULL,
    password text NOT NULL,
    isbanned boolean DEFAULT false NOT NULL,
    adddate date NOT NULL
);
    DROP TABLE public.bots;
       public         heap    postgres    false            w           0    0 
   TABLE bots    COMMENT     )   COMMENT ON TABLE public.bots IS 'TRIAL';
          public          postgres    false    205            x           0    0    COLUMN bots.id    COMMENT     -   COMMENT ON COLUMN public.bots.id IS 'TRIAL';
          public          postgres    false    205            y           0    0    COLUMN bots.telephone    COMMENT     4   COMMENT ON COLUMN public.bots.telephone IS 'TRIAL';
          public          postgres    false    205            z           0    0    COLUMN bots.password    COMMENT     3   COMMENT ON COLUMN public.bots.password IS 'TRIAL';
          public          postgres    false    205            {           0    0    COLUMN bots.isbanned    COMMENT     3   COMMENT ON COLUMN public.bots.isbanned IS 'TRIAL';
          public          postgres    false    205            |           0    0    COLUMN bots.adddate    COMMENT     2   COMMENT ON COLUMN public.bots.adddate IS 'TRIAL';
          public          postgres    false    205            �            1259    16408    bots_id_seq    SEQUENCE     �   CREATE SEQUENCE public.bots_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.bots_id_seq;
       public          postgres    false    205            }           0    0    bots_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.bots_id_seq OWNED BY public.bots.id;
          public          postgres    false    204            �            1259    16464    channel_entity    TABLE     �   CREATE TABLE public.channel_entity (
    id integer NOT NULL,
    channel text NOT NULL,
    join_time timestamp without time zone NOT NULL,
    leave_time timestamp without time zone NOT NULL,
    bot_id integer NOT NULL
);
 "   DROP TABLE public.channel_entity;
       public         heap    postgres    false            �            1259    16462    channel_entity_id_seq    SEQUENCE     �   ALTER TABLE public.channel_entity ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.channel_entity_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    214            �            1259    16422    errors    TABLE     i   CREATE TABLE public.errors (
    id integer NOT NULL,
    error text NOT NULL,
    date date NOT NULL
);
    DROP TABLE public.errors;
       public         heap    postgres    false            ~           0    0    TABLE errors    COMMENT     +   COMMENT ON TABLE public.errors IS 'TRIAL';
          public          postgres    false    207                       0    0    COLUMN errors.id    COMMENT     /   COMMENT ON COLUMN public.errors.id IS 'TRIAL';
          public          postgres    false    207            �           0    0    COLUMN errors.error    COMMENT     2   COMMENT ON COLUMN public.errors.error IS 'TRIAL';
          public          postgres    false    207            �           0    0    COLUMN errors.date    COMMENT     1   COMMENT ON COLUMN public.errors.date IS 'TRIAL';
          public          postgres    false    207            �            1259    16420    errors_id_seq    SEQUENCE     �   CREATE SEQUENCE public.errors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.errors_id_seq;
       public          postgres    false    207            �           0    0    errors_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.errors_id_seq OWNED BY public.errors.id;
          public          postgres    false    206            �            1259    16433    registredbots    TABLE     4  CREATE TABLE public.registredbots (
    id integer NOT NULL,
    phone text NOT NULL,
    api_id text NOT NULL,
    api_hash text NOT NULL,
    session text NOT NULL,
    isbanned boolean DEFAULT false NOT NULL,
    ltc_earned double precision DEFAULT 0 NOT NULL,
    wallet_id integer DEFAULT 1 NOT NULL
);
 !   DROP TABLE public.registredbots;
       public         heap    postgres    false            �           0    0    TABLE registredbots    COMMENT     2   COMMENT ON TABLE public.registredbots IS 'TRIAL';
          public          postgres    false    209            �           0    0    COLUMN registredbots.id    COMMENT     6   COMMENT ON COLUMN public.registredbots.id IS 'TRIAL';
          public          postgres    false    209            �           0    0    COLUMN registredbots.phone    COMMENT     9   COMMENT ON COLUMN public.registredbots.phone IS 'TRIAL';
          public          postgres    false    209            �           0    0    COLUMN registredbots.api_id    COMMENT     :   COMMENT ON COLUMN public.registredbots.api_id IS 'TRIAL';
          public          postgres    false    209            �           0    0    COLUMN registredbots.api_hash    COMMENT     <   COMMENT ON COLUMN public.registredbots.api_hash IS 'TRIAL';
          public          postgres    false    209            �           0    0    COLUMN registredbots.session    COMMENT     ;   COMMENT ON COLUMN public.registredbots.session IS 'TRIAL';
          public          postgres    false    209            �           0    0    COLUMN registredbots.isbanned    COMMENT     <   COMMENT ON COLUMN public.registredbots.isbanned IS 'TRIAL';
          public          postgres    false    209            �           0    0    COLUMN registredbots.ltc_earned    COMMENT     >   COMMENT ON COLUMN public.registredbots.ltc_earned IS 'TRIAL';
          public          postgres    false    209            �           0    0    COLUMN registredbots.wallet_id    COMMENT     =   COMMENT ON COLUMN public.registredbots.wallet_id IS 'TRIAL';
          public          postgres    false    209            �            1259    16431    registredbots_id_seq    SEQUENCE     �   CREATE SEQUENCE public.registredbots_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.registredbots_id_seq;
       public          postgres    false    209            �           0    0    registredbots_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.registredbots_id_seq OWNED BY public.registredbots.id;
          public          postgres    false    208            �            1259    16456    sqlite_sequence    TABLE     E   CREATE TABLE public.sqlite_sequence (
    name text,
    seq text
);
 #   DROP TABLE public.sqlite_sequence;
       public         heap    postgres    false            �           0    0    TABLE sqlite_sequence    COMMENT     4   COMMENT ON TABLE public.sqlite_sequence IS 'TRIAL';
          public          postgres    false    212            �           0    0    COLUMN sqlite_sequence.name    COMMENT     :   COMMENT ON COLUMN public.sqlite_sequence.name IS 'TRIAL';
          public          postgres    false    212            �           0    0    COLUMN sqlite_sequence.seq    COMMENT     9   COMMENT ON COLUMN public.sqlite_sequence.seq IS 'TRIAL';
          public          postgres    false    212            �            1259    16447    wallets    TABLE     M   CREATE TABLE public.wallets (
    id integer NOT NULL,
    wallet_id text
);
    DROP TABLE public.wallets;
       public         heap    postgres    false            �           0    0    TABLE wallets    COMMENT     ,   COMMENT ON TABLE public.wallets IS 'TRIAL';
          public          postgres    false    211            �           0    0    COLUMN wallets.id    COMMENT     0   COMMENT ON COLUMN public.wallets.id IS 'TRIAL';
          public          postgres    false    211            �           0    0    COLUMN wallets.wallet_id    COMMENT     7   COMMENT ON COLUMN public.wallets.wallet_id IS 'TRIAL';
          public          postgres    false    211            �            1259    16445    wallets_id_seq    SEQUENCE     �   CREATE SEQUENCE public.wallets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.wallets_id_seq;
       public          postgres    false    211            �           0    0    wallets_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.wallets_id_seq OWNED BY public.wallets.id;
          public          postgres    false    210            �
           2604    16402    bannedbots id    DEFAULT     n   ALTER TABLE ONLY public.bannedbots ALTER COLUMN id SET DEFAULT nextval('public.bannedbots_id_seq'::regclass);
 <   ALTER TABLE public.bannedbots ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    202    203    203            �
           2604    16413    bots id    DEFAULT     b   ALTER TABLE ONLY public.bots ALTER COLUMN id SET DEFAULT nextval('public.bots_id_seq'::regclass);
 6   ALTER TABLE public.bots ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205            �
           2604    16425 	   errors id    DEFAULT     f   ALTER TABLE ONLY public.errors ALTER COLUMN id SET DEFAULT nextval('public.errors_id_seq'::regclass);
 8   ALTER TABLE public.errors ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    206    207    207            �
           2604    16436    registredbots id    DEFAULT     t   ALTER TABLE ONLY public.registredbots ALTER COLUMN id SET DEFAULT nextval('public.registredbots_id_seq'::regclass);
 ?   ALTER TABLE public.registredbots ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208    209            �
           2604    16450 
   wallets id    DEFAULT     h   ALTER TABLE ONLY public.wallets ALTER COLUMN id SET DEFAULT nextval('public.wallets_id_seq'::regclass);
 9   ALTER TABLE public.wallets ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    211    211            �
           2606    16407    bannedbots bannedbots_pk 
   CONSTRAINT     V   ALTER TABLE ONLY public.bannedbots
    ADD CONSTRAINT bannedbots_pk PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.bannedbots DROP CONSTRAINT bannedbots_pk;
       public            postgres    false    203            �
           2606    16419    bots bots_pk 
   CONSTRAINT     J   ALTER TABLE ONLY public.bots
    ADD CONSTRAINT bots_pk PRIMARY KEY (id);
 6   ALTER TABLE ONLY public.bots DROP CONSTRAINT bots_pk;
       public            postgres    false    205            �
           2606    16471 "   channel_entity channel_entity_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.channel_entity
    ADD CONSTRAINT channel_entity_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.channel_entity DROP CONSTRAINT channel_entity_pkey;
       public            postgres    false    214            �
           2606    16430    errors errors_pk 
   CONSTRAINT     N   ALTER TABLE ONLY public.errors
    ADD CONSTRAINT errors_pk PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.errors DROP CONSTRAINT errors_pk;
       public            postgres    false    207            �
           2606    16444    registredbots registredbots_pk 
   CONSTRAINT     \   ALTER TABLE ONLY public.registredbots
    ADD CONSTRAINT registredbots_pk PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.registredbots DROP CONSTRAINT registredbots_pk;
       public            postgres    false    209            �
           2606    16455    wallets wallets_pk 
   CONSTRAINT     P   ALTER TABLE ONLY public.wallets
    ADD CONSTRAINT wallets_pk PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.wallets DROP CONSTRAINT wallets_pk;
       public            postgres    false    211           