# SyndProxy private pool

## Current pool

- Alive now: 1691
- Gold now: 679
- HTTP: 649 alive / 238 gold
- HTTPS: 518 alive / 132 gold
- SOCKS4: 216 alive / 143 gold
- SOCKS5: 308 alive / 166 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24500
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
