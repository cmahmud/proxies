# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 381
- HTTP: 218 alive / 79 gold
- HTTPS: 169 alive / 19 gold
- SOCKS4: 200 alive / 134 gold
- SOCKS5: 206 alive / 149 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27187
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
