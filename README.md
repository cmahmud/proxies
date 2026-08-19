# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 531
- HTTP: 370 alive / 155 gold
- HTTPS: 248 alive / 88 gold
- SOCKS4: 212 alive / 148 gold
- SOCKS5: 221 alive / 140 gold

## Historical pool

- Discovered: 119810
- Ever alive: 18035
- Ever gold: 711

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
