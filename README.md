# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 392
- HTTP: 108 alive / 66 gold
- HTTPS: 49 alive / 15 gold
- SOCKS4: 157 alive / 152 gold
- SOCKS5: 192 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33179
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
