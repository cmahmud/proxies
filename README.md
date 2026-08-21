# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 348
- HTTP: 250 alive / 75 gold
- HTTPS: 185 alive / 22 gold
- SOCKS4: 190 alive / 119 gold
- SOCKS5: 217 alive / 132 gold

## Historical pool

- Discovered: 157604
- Ever alive: 29776
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
