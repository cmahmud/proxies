# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 394
- HTTP: 181 alive / 70 gold
- HTTPS: 98 alive / 22 gold
- SOCKS4: 168 alive / 148 gold
- SOCKS5: 218 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39432
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
