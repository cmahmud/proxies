# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 219
- HTTP: 146 alive / 56 gold
- HTTPS: 133 alive / 11 gold
- SOCKS4: 88 alive / 69 gold
- SOCKS5: 142 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32683
- Ever gold: 1204

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
