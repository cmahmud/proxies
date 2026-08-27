# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 411
- HTTP: 110 alive / 65 gold
- HTTPS: 145 alive / 17 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41239
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
