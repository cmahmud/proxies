# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 405
- HTTP: 90 alive / 61 gold
- HTTPS: 72 alive / 19 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38525
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
