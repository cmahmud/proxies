# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 403
- HTTP: 100 alive / 63 gold
- HTTPS: 81 alive / 14 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39215
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
