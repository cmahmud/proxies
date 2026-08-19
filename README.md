# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 482
- HTTP: 370 alive / 126 gold
- HTTPS: 268 alive / 79 gold
- SOCKS4: 215 alive / 124 gold
- SOCKS5: 220 alive / 153 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17888
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
