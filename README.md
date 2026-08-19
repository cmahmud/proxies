# SyndProxy private pool

## Current pool

- Alive now: 1135
- Gold now: 360
- HTTP: 402 alive / 70 gold
- HTTPS: 259 alive / 13 gold
- SOCKS4: 221 alive / 130 gold
- SOCKS5: 253 alive / 147 gold

## Historical pool

- Discovered: 129303
- Ever alive: 20363
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
