# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 398
- HTTP: 108 alive / 60 gold
- HTTPS: 72 alive / 12 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38266
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
