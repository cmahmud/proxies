# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 447
- HTTP: 111 alive / 82 gold
- HTTPS: 91 alive / 33 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47007
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
