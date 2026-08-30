# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 451
- HTTP: 124 alive / 83 gold
- HTTPS: 148 alive / 39 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44744
- Ever gold: 1412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
