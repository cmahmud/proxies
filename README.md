# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 382
- HTTP: 237 alive / 79 gold
- HTTPS: 226 alive / 20 gold
- SOCKS4: 199 alive / 134 gold
- SOCKS5: 207 alive / 149 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27192
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
