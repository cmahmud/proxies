# SyndProxy private pool

## Current pool

- Alive now: 645
- Gold now: 201
- HTTP: 148 alive / 22 gold
- HTTPS: 101 alive / 9 gold
- SOCKS4: 186 alive / 89 gold
- SOCKS5: 210 alive / 81 gold

## Historical pool

- Discovered: 89658
- Ever alive: 7999
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
