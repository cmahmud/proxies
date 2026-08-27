# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 418
- HTTP: 103 alive / 71 gold
- HTTPS: 98 alive / 25 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41816
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
