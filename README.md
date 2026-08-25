# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 393
- HTTP: 102 alive / 63 gold
- HTTPS: 75 alive / 16 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 166 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37394
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
