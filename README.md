# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 385
- HTTP: 117 alive / 70 gold
- HTTPS: 160 alive / 18 gold
- SOCKS4: 162 alive / 147 gold
- SOCKS5: 174 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39771
- Ever gold: 1303

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
