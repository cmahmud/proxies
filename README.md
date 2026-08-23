# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 378
- HTTP: 92 alive / 62 gold
- HTTPS: 43 alive / 11 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 178 alive / 154 gold

## Historical pool

- Discovered: 174140
- Ever alive: 33068
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
