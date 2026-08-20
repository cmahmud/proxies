# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 381
- HTTP: 208 alive / 76 gold
- HTTPS: 209 alive / 20 gold
- SOCKS4: 200 alive / 134 gold
- SOCKS5: 209 alive / 151 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27201
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
