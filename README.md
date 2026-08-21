# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 438
- HTTP: 329 alive / 93 gold
- HTTPS: 247 alive / 26 gold
- SOCKS4: 234 alive / 150 gold
- SOCKS5: 253 alive / 169 gold

## Historical pool

- Discovered: 158927
- Ever alive: 30152
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
