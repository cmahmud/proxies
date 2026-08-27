# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 417
- HTTP: 98 alive / 75 gold
- HTTPS: 82 alive / 18 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 172 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41763
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
