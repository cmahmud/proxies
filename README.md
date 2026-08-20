# SyndProxy private pool

## Current pool

- Alive now: 1346
- Gold now: 579
- HTTP: 457 alive / 184 gold
- HTTPS: 337 alive / 98 gold
- SOCKS4: 245 alive / 140 gold
- SOCKS5: 307 alive / 157 gold

## Historical pool

- Discovered: 138941
- Ever alive: 23200
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
