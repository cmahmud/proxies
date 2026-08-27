# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 416
- HTTP: 106 alive / 73 gold
- HTTPS: 137 alive / 20 gold
- SOCKS4: 184 alive / 157 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42105
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
