# SyndProxy private pool

## Current pool

- Alive now: 1106
- Gold now: 391
- HTTP: 379 alive / 97 gold
- HTTPS: 263 alive / 29 gold
- SOCKS4: 203 alive / 121 gold
- SOCKS5: 261 alive / 144 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28085
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
