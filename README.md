# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 422
- HTTP: 103 alive / 77 gold
- HTTPS: 114 alive / 18 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42116
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
