# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 441
- HTTP: 332 alive / 94 gold
- HTTPS: 240 alive / 26 gold
- SOCKS4: 229 alive / 151 gold
- SOCKS5: 246 alive / 170 gold

## Historical pool

- Discovered: 158927
- Ever alive: 30155
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
