# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 200
- HTTP: 180 alive / 44 gold
- HTTPS: 58 alive / 6 gold
- SOCKS4: 98 alive / 66 gold
- SOCKS5: 156 alive / 84 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32733
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
