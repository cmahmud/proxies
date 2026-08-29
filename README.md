# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 394
- HTTP: 88 alive / 63 gold
- HTTPS: 53 alive / 20 gold
- SOCKS4: 161 alive / 153 gold
- SOCKS5: 168 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43649
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
