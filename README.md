# SyndProxy private pool

## Current pool

- Alive now: 1301
- Gold now: 517
- HTTP: 498 alive / 183 gold
- HTTPS: 353 alive / 51 gold
- SOCKS4: 204 alive / 123 gold
- SOCKS5: 246 alive / 160 gold

## Historical pool

- Discovered: 125668
- Ever alive: 19647
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
