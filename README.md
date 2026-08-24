# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 371
- HTTP: 91 alive / 57 gold
- HTTPS: 52 alive / 12 gold
- SOCKS4: 156 alive / 150 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 175898
- Ever alive: 33198
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
