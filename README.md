# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 480
- HTTP: 333 alive / 120 gold
- HTTPS: 215 alive / 72 gold
- SOCKS4: 230 alive / 140 gold
- SOCKS5: 268 alive / 148 gold

## Historical pool

- Discovered: 113575
- Ever alive: 16875
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
