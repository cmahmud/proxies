# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 375
- HTTP: 242 alive / 83 gold
- HTTPS: 146 alive / 23 gold
- SOCKS4: 200 alive / 114 gold
- SOCKS5: 246 alive / 155 gold

## Historical pool

- Discovered: 166560
- Ever alive: 32402
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
