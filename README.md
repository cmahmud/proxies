# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 355
- HTTP: 353 alive / 72 gold
- HTTPS: 199 alive / 15 gold
- SOCKS4: 235 alive / 146 gold
- SOCKS5: 215 alive / 122 gold

## Historical pool

- Discovered: 110913
- Ever alive: 16044
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
