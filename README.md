# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 436
- HTTP: 138 alive / 81 gold
- HTTPS: 94 alive / 25 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34586
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
