# SyndProxy private pool

## Current pool

- Alive now: 854
- Gold now: 408
- HTTP: 238 alive / 91 gold
- HTTPS: 173 alive / 25 gold
- SOCKS4: 194 alive / 137 gold
- SOCKS5: 249 alive / 155 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29068
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
