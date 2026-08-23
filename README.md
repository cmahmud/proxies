# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 218
- HTTP: 149 alive / 56 gold
- HTTPS: 131 alive / 11 gold
- SOCKS4: 89 alive / 68 gold
- SOCKS5: 149 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32683
- Ever gold: 1204

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
