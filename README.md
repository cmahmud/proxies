# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 365
- HTTP: 302 alive / 74 gold
- HTTPS: 233 alive / 18 gold
- SOCKS4: 250 alive / 151 gold
- SOCKS5: 212 alive / 122 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15925
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
