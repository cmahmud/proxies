# SyndProxy private pool

## Current pool

- Alive now: 838
- Gold now: 274
- HTTP: 245 alive / 31 gold
- HTTPS: 160 alive / 5 gold
- SOCKS4: 229 alive / 134 gold
- SOCKS5: 204 alive / 104 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11452
- Ever gold: 383

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
