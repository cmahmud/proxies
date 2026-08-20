# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 384
- HTTP: 284 alive / 95 gold
- HTTPS: 229 alive / 27 gold
- SOCKS4: 218 alive / 129 gold
- SOCKS5: 238 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25065
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
