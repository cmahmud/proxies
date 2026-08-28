# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 441
- HTTP: 121 alive / 87 gold
- HTTPS: 145 alive / 23 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42222
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
