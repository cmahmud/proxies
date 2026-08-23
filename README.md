# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 373
- HTTP: 90 alive / 61 gold
- HTTPS: 37 alive / 10 gold
- SOCKS4: 160 alive / 150 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 174159
- Ever alive: 33077
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
