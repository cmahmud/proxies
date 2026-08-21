# SyndProxy private pool

## Current pool

- Alive now: 1093
- Gold now: 427
- HTTP: 333 alive / 90 gold
- HTTPS: 264 alive / 27 gold
- SOCKS4: 238 alive / 145 gold
- SOCKS5: 258 alive / 165 gold

## Historical pool

- Discovered: 158927
- Ever alive: 30150
- Ever gold: 1142

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
