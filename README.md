# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 316
- HTTP: 129 alive / 37 gold
- HTTPS: 51 alive / 7 gold
- SOCKS4: 166 alive / 133 gold
- SOCKS5: 178 alive / 139 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32786
- Ever gold: 1211

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
