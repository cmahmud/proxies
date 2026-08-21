# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 377
- HTTP: 326 alive / 85 gold
- HTTPS: 249 alive / 23 gold
- SOCKS4: 179 alive / 119 gold
- SOCKS5: 236 alive / 150 gold

## Historical pool

- Discovered: 158225
- Ever alive: 29871
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
