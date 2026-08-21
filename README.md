# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 429
- HTTP: 320 alive / 91 gold
- HTTPS: 261 alive / 28 gold
- SOCKS4: 231 alive / 145 gold
- SOCKS5: 253 alive / 165 gold

## Historical pool

- Discovered: 158927
- Ever alive: 30151
- Ever gold: 1142

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
