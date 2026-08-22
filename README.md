# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 397
- HTTP: 319 alive / 85 gold
- HTTPS: 185 alive / 29 gold
- SOCKS4: 206 alive / 146 gold
- SOCKS5: 232 alive / 137 gold

## Historical pool

- Discovered: 167118
- Ever alive: 32529
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
