# SyndProxy validated proxy pool

## Current pool

- Alive now: 392
- Gold now: 217
- HTTP: 146 alive / 56 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 75 alive / 68 gold
- SOCKS5: 120 alive / 81 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32689
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
