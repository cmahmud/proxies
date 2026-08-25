# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 401
- HTTP: 90 alive / 63 gold
- HTTPS: 83 alive / 21 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37591
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
