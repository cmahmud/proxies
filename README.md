# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 341
- HTTP: 349 alive / 58 gold
- HTTPS: 212 alive / 16 gold
- SOCKS4: 209 alive / 134 gold
- SOCKS5: 210 alive / 133 gold

## Historical pool

- Discovered: 129236
- Ever alive: 20046
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
