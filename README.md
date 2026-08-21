# SyndProxy private pool

## Current pool

- Alive now: 835
- Gold now: 348
- HTTP: 224 alive / 75 gold
- HTTPS: 205 alive / 22 gold
- SOCKS4: 187 alive / 120 gold
- SOCKS5: 219 alive / 131 gold

## Historical pool

- Discovered: 157604
- Ever alive: 29776
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
