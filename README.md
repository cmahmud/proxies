# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 472
- HTTP: 140 alive / 95 gold
- HTTPS: 129 alive / 38 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46942
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
