# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 322
- HTTP: 131 alive / 37 gold
- HTTPS: 50 alive / 8 gold
- SOCKS4: 165 alive / 135 gold
- SOCKS5: 178 alive / 142 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32786
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
