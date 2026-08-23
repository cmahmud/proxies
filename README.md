# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 122
- HTTP: 196 alive / 37 gold
- HTTPS: 80 alive / 4 gold
- SOCKS4: 150 alive / 0 gold
- SOCKS5: 203 alive / 81 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32679
- Ever gold: 1193

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
