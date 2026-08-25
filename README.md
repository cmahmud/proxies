# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 404
- HTTP: 88 alive / 66 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37695
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
