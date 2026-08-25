# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 409
- HTTP: 99 alive / 69 gold
- HTTPS: 61 alive / 21 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 170 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37144
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
