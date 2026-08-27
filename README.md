# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 412
- HTTP: 117 alive / 69 gold
- HTTPS: 167 alive / 15 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40927
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
