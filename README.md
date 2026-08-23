# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 373
- HTTP: 88 alive / 58 gold
- HTTPS: 38 alive / 11 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 187 alive / 153 gold

## Historical pool

- Discovered: 174140
- Ever alive: 33065
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
