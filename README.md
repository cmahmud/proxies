# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 382
- HTTP: 324 alive / 87 gold
- HTTPS: 197 alive / 25 gold
- SOCKS4: 224 alive / 144 gold
- SOCKS5: 234 alive / 126 gold

## Historical pool

- Discovered: 165832
- Ever alive: 32354
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
