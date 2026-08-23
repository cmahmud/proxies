# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 376
- HTTP: 87 alive / 60 gold
- HTTPS: 38 alive / 12 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 187 alive / 153 gold

## Historical pool

- Discovered: 174140
- Ever alive: 33063
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
