# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 356
- HTTP: 282 alive / 52 gold
- HTTPS: 207 alive / 16 gold
- SOCKS4: 225 alive / 147 gold
- SOCKS5: 245 alive / 141 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14768
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
