# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 396
- HTTP: 296 alive / 86 gold
- HTTPS: 189 alive / 29 gold
- SOCKS4: 201 alive / 146 gold
- SOCKS5: 229 alive / 135 gold

## Historical pool

- Discovered: 167118
- Ever alive: 32529
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
