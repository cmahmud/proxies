# SyndProxy private pool

## Current pool

- Alive now: 1016
- Gold now: 345
- HTTP: 315 alive / 68 gold
- HTTPS: 245 alive / 18 gold
- SOCKS4: 226 alive / 144 gold
- SOCKS5: 230 alive / 115 gold

## Historical pool

- Discovered: 111009
- Ever alive: 16104
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
