# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 509
- HTTP: 379 alive / 140 gold
- HTTPS: 261 alive / 83 gold
- SOCKS4: 234 alive / 151 gold
- SOCKS5: 201 alive / 135 gold

## Historical pool

- Discovered: 119808
- Ever alive: 17965
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
