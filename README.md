# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 366
- HTTP: 281 alive / 84 gold
- HTTPS: 243 alive / 25 gold
- SOCKS4: 218 alive / 123 gold
- SOCKS5: 203 alive / 134 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29804
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
