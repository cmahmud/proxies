# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 344
- HTTP: 110 alive / 40 gold
- HTTPS: 78 alive / 10 gold
- SOCKS4: 157 alive / 153 gold
- SOCKS5: 179 alive / 141 gold

## Historical pool

- Discovered: 171038
- Ever alive: 32814
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
