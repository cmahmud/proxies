# SyndProxy private pool

## Current pool

- Alive now: 811
- Gold now: 383
- HTTP: 230 alive / 79 gold
- HTTPS: 161 alive / 21 gold
- SOCKS4: 210 alive / 147 gold
- SOCKS5: 210 alive / 136 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31876
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
