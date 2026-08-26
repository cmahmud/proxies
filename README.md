# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 405
- HTTP: 107 alive / 63 gold
- HTTPS: 60 alive / 18 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38684
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
