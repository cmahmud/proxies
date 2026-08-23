# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 390
- HTTP: 127 alive / 66 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 207 alive / 158 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33177
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
