# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 383
- HTTP: 223 alive / 80 gold
- HTTPS: 121 alive / 16 gold
- SOCKS4: 228 alive / 152 gold
- SOCKS5: 198 alive / 135 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25467
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
