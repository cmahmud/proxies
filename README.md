# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 394
- HTTP: 73 alive / 52 gold
- HTTPS: 37 alive / 17 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42856
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
