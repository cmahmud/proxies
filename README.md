# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 416
- HTTP: 87 alive / 69 gold
- HTTPS: 104 alive / 19 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42580
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
