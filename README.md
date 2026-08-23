# SyndProxy validated proxy pool

## Current pool

- Alive now: 395
- Gold now: 217
- HTTP: 135 alive / 55 gold
- HTTPS: 51 alive / 10 gold
- SOCKS4: 90 alive / 68 gold
- SOCKS5: 119 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32695
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
