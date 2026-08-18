# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 352
- HTTP: 274 alive / 53 gold
- HTTPS: 199 alive / 15 gold
- SOCKS4: 246 alive / 147 gold
- SOCKS5: 233 alive / 137 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14721
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
