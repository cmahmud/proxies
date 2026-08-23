# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 374
- HTTP: 89 alive / 56 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 179 alive / 154 gold

## Historical pool

- Discovered: 174140
- Ever alive: 33062
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
