# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 411
- HTTP: 115 alive / 65 gold
- HTTPS: 106 alive / 17 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39309
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
