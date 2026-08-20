# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 388
- HTTP: 204 alive / 80 gold
- HTTPS: 169 alive / 21 gold
- SOCKS4: 196 alive / 135 gold
- SOCKS5: 208 alive / 152 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27174
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
