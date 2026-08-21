# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 425
- HTTP: 323 alive / 89 gold
- HTTPS: 220 alive / 25 gold
- SOCKS4: 215 alive / 154 gold
- SOCKS5: 235 alive / 157 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30096
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
