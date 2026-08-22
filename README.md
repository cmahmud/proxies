# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 344
- HTTP: 327 alive / 82 gold
- HTTPS: 259 alive / 31 gold
- SOCKS4: 204 alive / 139 gold
- SOCKS5: 199 alive / 92 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32517
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
