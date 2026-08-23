# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 331
- HTTP: 104 alive / 37 gold
- HTTPS: 90 alive / 5 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 186 alive / 138 gold

## Historical pool

- Discovered: 171581
- Ever alive: 32901
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
