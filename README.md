# SyndProxy private pool

## Current pool

- Alive now: 1112
- Gold now: 486
- HTTP: 432 alive / 162 gold
- HTTPS: 245 alive / 82 gold
- SOCKS4: 200 alive / 110 gold
- SOCKS5: 235 alive / 132 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18764
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
