# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 497
- HTTP: 304 alive / 148 gold
- HTTPS: 243 alive / 90 gold
- SOCKS4: 192 alive / 124 gold
- SOCKS5: 215 alive / 135 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17598
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
