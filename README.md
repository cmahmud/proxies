# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 420
- HTTP: 103 alive / 77 gold
- HTTPS: 122 alive / 17 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42151
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
