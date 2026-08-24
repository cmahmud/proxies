# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 394
- HTTP: 120 alive / 60 gold
- HTTPS: 49 alive / 15 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 194 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33519
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
