# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 468
- HTTP: 130 alive / 93 gold
- HTTPS: 108 alive / 36 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 213 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46417
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
