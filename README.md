# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 352
- HTTP: 332 alive / 71 gold
- HTTPS: 216 alive / 18 gold
- SOCKS4: 234 alive / 143 gold
- SOCKS5: 209 alive / 120 gold

## Historical pool

- Discovered: 110913
- Ever alive: 16058
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
