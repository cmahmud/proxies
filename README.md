# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 400
- HTTP: 276 alive / 94 gold
- HTTPS: 219 alive / 34 gold
- SOCKS4: 202 alive / 144 gold
- SOCKS5: 231 alive / 128 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30952
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
