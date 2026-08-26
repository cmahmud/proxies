# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 409
- HTTP: 88 alive / 63 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38627
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
