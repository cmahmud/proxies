# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 408
- HTTP: 359 alive / 105 gold
- HTTPS: 262 alive / 24 gold
- SOCKS4: 214 alive / 135 gold
- SOCKS5: 239 alive / 144 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28268
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
