# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 532
- HTTP: 363 alive / 162 gold
- HTTPS: 245 alive / 89 gold
- SOCKS4: 207 alive / 134 gold
- SOCKS5: 225 alive / 147 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18714
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
