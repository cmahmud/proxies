# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 393
- HTTP: 77 alive / 53 gold
- HTTPS: 54 alive / 17 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41580
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
