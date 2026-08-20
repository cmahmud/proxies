# SyndProxy private pool

## Current pool

- Alive now: 1570
- Gold now: 620
- HTTP: 615 alive / 224 gold
- HTTPS: 496 alive / 113 gold
- SOCKS4: 207 alive / 137 gold
- SOCKS5: 252 alive / 146 gold

## Historical pool

- Discovered: 141135
- Ever alive: 23823
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
