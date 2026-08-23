# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 388
- HTTP: 113 alive / 66 gold
- HTTPS: 48 alive / 14 gold
- SOCKS4: 168 alive / 151 gold
- SOCKS5: 212 alive / 157 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33178
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
