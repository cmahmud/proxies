# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 407
- HTTP: 110 alive / 69 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 166 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37301
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
