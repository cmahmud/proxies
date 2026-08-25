# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 409
- HTTP: 115 alive / 71 gold
- HTTPS: 82 alive / 21 gold
- SOCKS4: 162 alive / 158 gold
- SOCKS5: 169 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37180
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
