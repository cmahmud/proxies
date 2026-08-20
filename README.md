# SyndProxy private pool

## Current pool

- Alive now: 1539
- Gold now: 621
- HTTP: 593 alive / 207 gold
- HTTPS: 486 alive / 113 gold
- SOCKS4: 225 alive / 144 gold
- SOCKS5: 235 alive / 157 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24030
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
