# SyndProxy private pool

## Current pool

- Alive now: 1226
- Gold now: 584
- HTTP: 415 alive / 199 gold
- HTTPS: 335 alive / 98 gold
- SOCKS4: 218 alive / 139 gold
- SOCKS5: 258 alive / 148 gold

## Historical pool

- Discovered: 138948
- Ever alive: 23384
- Ever gold: 919

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
