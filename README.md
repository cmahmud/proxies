# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 391
- HTTP: 114 alive / 66 gold
- HTTPS: 56 alive / 12 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 185 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33184
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
