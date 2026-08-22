# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 444
- HTTP: 274 alive / 84 gold
- HTTPS: 229 alive / 32 gold
- SOCKS4: 235 alive / 156 gold
- SOCKS5: 254 alive / 172 gold

## Historical pool

- Discovered: 163874
- Ever alive: 32017
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
