# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 388
- HTTP: 213 alive / 81 gold
- HTTPS: 164 alive / 20 gold
- SOCKS4: 209 alive / 136 gold
- SOCKS5: 208 alive / 151 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27183
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
