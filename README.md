# SyndProxy private pool

## Current pool

- Alive now: 561
- Gold now: 213
- HTTP: 136 alive / 26 gold
- HTTPS: 75 alive / 8 gold
- SOCKS4: 169 alive / 109 gold
- SOCKS5: 181 alive / 70 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8360
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
