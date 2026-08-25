# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 401
- HTTP: 86 alive / 63 gold
- HTTPS: 75 alive / 18 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 179 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37616
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
