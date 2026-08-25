# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 427
- HTTP: 113 alive / 75 gold
- HTTPS: 104 alive / 25 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35016
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
