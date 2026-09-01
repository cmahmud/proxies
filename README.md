# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 447
- HTTP: 105 alive / 79 gold
- HTTPS: 109 alive / 30 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 186 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47379
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
