# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 394
- HTTP: 77 alive / 58 gold
- HTTPS: 60 alive / 15 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42820
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
