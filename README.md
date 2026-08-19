# SyndProxy private pool

## Current pool

- Alive now: 1117
- Gold now: 535
- HTTP: 426 alive / 159 gold
- HTTPS: 294 alive / 93 gold
- SOCKS4: 195 alive / 139 gold
- SOCKS5: 202 alive / 144 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19878
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
