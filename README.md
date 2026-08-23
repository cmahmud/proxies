# SyndProxy validated proxy pool

## Current pool

- Alive now: 338
- Gold now: 207
- HTTP: 106 alive / 46 gold
- HTTPS: 43 alive / 6 gold
- SOCKS4: 80 alive / 66 gold
- SOCKS5: 109 alive / 89 gold

## Historical pool

- Discovered: 170283
- Ever alive: 32757
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
