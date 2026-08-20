# SyndProxy private pool

## Current pool

- Alive now: 1556
- Gold now: 621
- HTTP: 586 alive / 215 gold
- HTTPS: 507 alive / 119 gold
- SOCKS4: 235 alive / 153 gold
- SOCKS5: 228 alive / 134 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23757
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
