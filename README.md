# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 366
- HTTP: 334 alive / 86 gold
- HTTPS: 231 alive / 28 gold
- SOCKS4: 195 alive / 117 gold
- SOCKS5: 225 alive / 135 gold

## Historical pool

- Discovered: 165018
- Ever alive: 32266
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
