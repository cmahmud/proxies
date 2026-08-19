# SyndProxy private pool

## Current pool

- Alive now: 1219
- Gold now: 462
- HTTP: 448 alive / 126 gold
- HTTPS: 290 alive / 75 gold
- SOCKS4: 225 alive / 118 gold
- SOCKS5: 256 alive / 143 gold

## Historical pool

- Discovered: 117109
- Ever alive: 17257
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
