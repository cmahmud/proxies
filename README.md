# SyndProxy private pool

## Current pool

- Alive now: 1198
- Gold now: 409
- HTTP: 422 alive / 92 gold
- HTTPS: 246 alive / 18 gold
- SOCKS4: 236 alive / 143 gold
- SOCKS5: 294 alive / 156 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20871
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
