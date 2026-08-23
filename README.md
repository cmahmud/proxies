# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 394
- HTTP: 110 alive / 67 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 158 alive / 154 gold
- SOCKS5: 197 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33184
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
