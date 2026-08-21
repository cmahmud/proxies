# SyndProxy private pool

## Current pool

- Alive now: 788
- Gold now: 347
- HTTP: 233 alive / 76 gold
- HTTPS: 146 alive / 20 gold
- SOCKS4: 204 alive / 120 gold
- SOCKS5: 205 alive / 131 gold

## Historical pool

- Discovered: 157663
- Ever alive: 29782
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
