# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 376
- HTTP: 100 alive / 59 gold
- HTTPS: 54 alive / 14 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 171 alive / 152 gold

## Historical pool

- Discovered: 175898
- Ever alive: 33198
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
