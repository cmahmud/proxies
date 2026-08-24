# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 371
- HTTP: 94 alive / 55 gold
- HTTPS: 58 alive / 14 gold
- SOCKS4: 157 alive / 150 gold
- SOCKS5: 172 alive / 152 gold

## Historical pool

- Discovered: 175898
- Ever alive: 33198
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
