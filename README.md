# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 335
- HTTP: 114 alive / 36 gold
- HTTPS: 47 alive / 8 gold
- SOCKS4: 162 alive / 149 gold
- SOCKS5: 175 alive / 142 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32786
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
