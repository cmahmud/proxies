# SyndProxy private pool

## Current pool

- Alive now: 1143
- Gold now: 499
- HTTP: 392 alive / 123 gold
- HTTPS: 252 alive / 74 gold
- SOCKS4: 229 alive / 149 gold
- SOCKS5: 270 alive / 153 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17027
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
