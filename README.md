# SyndProxy private pool

## Current pool

- Alive now: 734
- Gold now: 376
- HTTP: 206 alive / 74 gold
- HTTPS: 100 alive / 15 gold
- SOCKS4: 225 alive / 144 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25432
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
