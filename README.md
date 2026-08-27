# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 416
- HTTP: 99 alive / 69 gold
- HTTPS: 110 alive / 21 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41940
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
