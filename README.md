# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 489
- HTTP: 386 alive / 125 gold
- HTTPS: 206 alive / 73 gold
- SOCKS4: 203 alive / 141 gold
- SOCKS5: 255 alive / 150 gold

## Historical pool

- Discovered: 114275
- Ever alive: 16921
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
