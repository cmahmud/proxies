# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 395
- HTTP: 107 alive / 67 gold
- HTTPS: 50 alive / 14 gold
- SOCKS4: 158 alive / 154 gold
- SOCKS5: 202 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33183
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
