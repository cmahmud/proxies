# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 220
- HTTP: 152 alive / 57 gold
- HTTPS: 113 alive / 11 gold
- SOCKS4: 90 alive / 68 gold
- SOCKS5: 151 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32683
- Ever gold: 1203

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
