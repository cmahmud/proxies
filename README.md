# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 471
- HTTP: 132 alive / 96 gold
- HTTPS: 114 alive / 41 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 201 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44847
- Ever gold: 1416

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
