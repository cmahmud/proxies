# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 394
- HTTP: 311 alive / 84 gold
- HTTPS: 248 alive / 23 gold
- SOCKS4: 206 alive / 135 gold
- SOCKS5: 209 alive / 152 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27272
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
