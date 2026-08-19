# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 335
- HTTP: 345 alive / 56 gold
- HTTPS: 213 alive / 13 gold
- SOCKS4: 212 alive / 133 gold
- SOCKS5: 199 alive / 133 gold

## Historical pool

- Discovered: 129234
- Ever alive: 20034
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
