# SyndProxy private pool

## Current pool

- Alive now: 787
- Gold now: 395
- HTTP: 199 alive / 84 gold
- HTTPS: 137 alive / 26 gold
- SOCKS4: 217 alive / 135 gold
- SOCKS5: 234 alive / 150 gold

## Historical pool

- Discovered: 154727
- Ever alive: 29161
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
