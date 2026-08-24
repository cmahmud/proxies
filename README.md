# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 379
- HTTP: 101 alive / 45 gold
- HTTPS: 39 alive / 11 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33541
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
