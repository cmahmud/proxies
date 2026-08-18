# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 279
- HTTP: 346 alive / 27 gold
- HTTPS: 254 alive / 5 gold
- SOCKS4: 218 alive / 126 gold
- SOCKS5: 232 alive / 121 gold

## Historical pool

- Discovered: 102838
- Ever alive: 13090
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
