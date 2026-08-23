# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 123
- HTTP: 212 alive / 37 gold
- HTTPS: 80 alive / 4 gold
- SOCKS4: 106 alive / 0 gold
- SOCKS5: 230 alive / 82 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32675
- Ever gold: 1193

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
