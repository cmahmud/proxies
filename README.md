# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 448
- HTTP: 108 alive / 79 gold
- HTTPS: 106 alive / 31 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47379
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
