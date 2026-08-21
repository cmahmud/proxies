# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 361
- HTTP: 327 alive / 81 gold
- HTTPS: 210 alive / 18 gold
- SOCKS4: 215 alive / 119 gold
- SOCKS5: 205 alive / 143 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29807
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
