# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 365
- HTTP: 93 alive / 51 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 179 alive / 153 gold

## Historical pool

- Discovered: 174122
- Ever alive: 33054
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
