# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 359
- HTTP: 246 alive / 83 gold
- HTTPS: 212 alive / 23 gold
- SOCKS4: 185 alive / 120 gold
- SOCKS5: 216 alive / 133 gold

## Historical pool

- Discovered: 157604
- Ever alive: 29776
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
