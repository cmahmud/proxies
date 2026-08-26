# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 378
- HTTP: 125 alive / 69 gold
- HTTPS: 166 alive / 14 gold
- SOCKS4: 160 alive / 145 gold
- SOCKS5: 172 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39795
- Ever gold: 1303

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
