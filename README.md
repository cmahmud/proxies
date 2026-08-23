# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 356
- HTTP: 88 alive / 34 gold
- HTTPS: 37 alive / 10 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 175 alive / 156 gold

## Historical pool

- Discovered: 171825
- Ever alive: 32948
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
