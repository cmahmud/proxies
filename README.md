# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 387
- HTTP: 96 alive / 60 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 159 alive / 156 gold
- SOCKS5: 177 alive / 159 gold

## Historical pool

- Discovered: 175898
- Ever alive: 33195
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
