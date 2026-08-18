# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 356
- HTTP: 332 alive / 59 gold
- HTTPS: 192 alive / 14 gold
- SOCKS4: 240 alive / 146 gold
- SOCKS5: 227 alive / 137 gold

## Historical pool

- Discovered: 107156
- Ever alive: 15139
- Ever gold: 483

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
