# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 404
- HTTP: 109 alive / 66 gold
- HTTPS: 160 alive / 10 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40943
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
