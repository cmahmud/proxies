# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 432
- HTTP: 321 alive / 91 gold
- HTTPS: 233 alive / 32 gold
- SOCKS4: 215 alive / 143 gold
- SOCKS5: 246 alive / 166 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31241
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
