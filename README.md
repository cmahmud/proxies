# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 421
- HTTP: 110 alive / 63 gold
- HTTPS: 86 alive / 25 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35778
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
