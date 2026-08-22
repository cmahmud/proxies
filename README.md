# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 377
- HTTP: 279 alive / 84 gold
- HTTPS: 233 alive / 26 gold
- SOCKS4: 233 alive / 125 gold
- SOCKS5: 233 alive / 142 gold

## Historical pool

- Discovered: 164909
- Ever alive: 32119
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
