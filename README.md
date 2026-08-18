# SyndProxy private pool

## Current pool

- Alive now: 672
- Gold now: 254
- HTTP: 175 alive / 32 gold
- HTTPS: 97 alive / 8 gold
- SOCKS4: 191 alive / 112 gold
- SOCKS5: 209 alive / 102 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10238
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
