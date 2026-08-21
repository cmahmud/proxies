# SyndProxy private pool

## Current pool

- Alive now: 1151
- Gold now: 400
- HTTP: 405 alive / 112 gold
- HTTPS: 283 alive / 30 gold
- SOCKS4: 220 alive / 117 gold
- SOCKS5: 243 alive / 141 gold

## Historical pool

- Discovered: 160249
- Ever alive: 30678
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
