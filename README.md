# SyndProxy private pool

## Current pool

- Alive now: 1166
- Gold now: 394
- HTTP: 413 alive / 99 gold
- HTTPS: 286 alive / 28 gold
- SOCKS4: 204 alive / 122 gold
- SOCKS5: 263 alive / 145 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28089
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
