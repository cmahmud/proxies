# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 326
- HTTP: 130 alive / 37 gold
- HTTPS: 48 alive / 8 gold
- SOCKS4: 165 alive / 139 gold
- SOCKS5: 177 alive / 142 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32786
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
