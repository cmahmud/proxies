# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 416
- HTTP: 114 alive / 69 gold
- HTTPS: 132 alive / 18 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41336
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
