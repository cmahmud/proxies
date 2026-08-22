# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 407
- HTTP: 328 alive / 84 gold
- HTTPS: 245 alive / 24 gold
- SOCKS4: 229 alive / 149 gold
- SOCKS5: 250 alive / 150 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32287
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
