# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 385
- HTTP: 238 alive / 81 gold
- HTTPS: 128 alive / 16 gold
- SOCKS4: 220 alive / 152 gold
- SOCKS5: 197 alive / 136 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25466
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
