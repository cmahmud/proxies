# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 409
- HTTP: 94 alive / 62 gold
- HTTPS: 74 alive / 22 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37030
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
