# SyndProxy private pool

## Current pool

- Alive now: 1417
- Gold now: 409
- HTTP: 498 alive / 90 gold
- HTTPS: 335 alive / 17 gold
- SOCKS4: 261 alive / 151 gold
- SOCKS5: 323 alive / 151 gold

## Historical pool

- Discovered: 133965
- Ever alive: 21665
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
