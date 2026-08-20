# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 376
- HTTP: 240 alive / 76 gold
- HTTPS: 120 alive / 15 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 193 alive / 135 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25461
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
