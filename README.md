# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 401
- HTTP: 159 alive / 69 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 195 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33305
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
