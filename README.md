# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 122
- HTTP: 216 alive / 37 gold
- HTTPS: 81 alive / 3 gold
- SOCKS4: 100 alive / 0 gold
- SOCKS5: 240 alive / 82 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32675
- Ever gold: 1193

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
