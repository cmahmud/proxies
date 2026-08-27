# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 416
- HTTP: 103 alive / 76 gold
- HTTPS: 120 alive / 22 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41854
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
