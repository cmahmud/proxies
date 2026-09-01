# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 447
- HTTP: 110 alive / 82 gold
- HTTPS: 88 alive / 33 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47006
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
