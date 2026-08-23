# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 374
- HTTP: 91 alive / 57 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 171 alive / 151 gold
- SOCKS5: 177 alive / 154 gold

## Historical pool

- Discovered: 174140
- Ever alive: 33062
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
