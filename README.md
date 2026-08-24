# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 378
- HTTP: 94 alive / 51 gold
- HTTPS: 60 alive / 11 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33444
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
