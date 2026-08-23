# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 374
- HTTP: 98 alive / 58 gold
- HTTPS: 46 alive / 11 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 183 alive / 154 gold

## Historical pool

- Discovered: 174133
- Ever alive: 33061
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
