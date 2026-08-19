# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 359
- HTTP: 337 alive / 68 gold
- HTTPS: 173 alive / 18 gold
- SOCKS4: 250 alive / 154 gold
- SOCKS5: 214 alive / 119 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16007
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
