# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 274
- HTTP: 126 alive / 37 gold
- HTTPS: 53 alive / 4 gold
- SOCKS4: 166 alive / 93 gold
- SOCKS5: 179 alive / 140 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32786
- Ever gold: 1210

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
