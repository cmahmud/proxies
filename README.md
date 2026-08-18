# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 202
- HTTP: 434 alive / 23 gold
- HTTPS: 144 alive / 8 gold
- SOCKS4: 214 alive / 100 gold
- SOCKS5: 202 alive / 71 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8336
- Ever gold: 348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
