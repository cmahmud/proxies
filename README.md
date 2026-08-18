# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 239
- HTTP: 362 alive / 30 gold
- HTTPS: 173 alive / 8 gold
- SOCKS4: 279 alive / 115 gold
- SOCKS5: 218 alive / 86 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6878
- Ever gold: 318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
