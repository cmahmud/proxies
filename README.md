# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 324
- HTTP: 252 alive / 39 gold
- HTTPS: 177 alive / 9 gold
- SOCKS4: 214 alive / 140 gold
- SOCKS5: 228 alive / 136 gold

## Historical pool

- Discovered: 102931
- Ever alive: 13994
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
