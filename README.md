# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 449
- HTTP: 308 alive / 96 gold
- HTTPS: 192 alive / 30 gold
- SOCKS4: 225 alive / 156 gold
- SOCKS5: 245 alive / 167 gold

## Historical pool

- Discovered: 167119
- Ever alive: 32535
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
