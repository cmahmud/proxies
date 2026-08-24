# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 401
- HTTP: 158 alive / 69 gold
- HTTPS: 48 alive / 14 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 195 alive / 162 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33305
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
