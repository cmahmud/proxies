# SyndProxy private pool

## Current pool

- Alive now: 1138
- Gold now: 533
- HTTP: 434 alive / 157 gold
- HTTPS: 295 alive / 93 gold
- SOCKS4: 204 alive / 139 gold
- SOCKS5: 205 alive / 144 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19883
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
