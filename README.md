# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 409
- HTTP: 90 alive / 61 gold
- HTTPS: 72 alive / 22 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37030
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
