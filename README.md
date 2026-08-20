# SyndProxy private pool

## Current pool

- Alive now: 798
- Gold now: 382
- HTTP: 186 alive / 75 gold
- HTTPS: 168 alive / 20 gold
- SOCKS4: 222 alive / 149 gold
- SOCKS5: 222 alive / 138 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26893
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
