# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 389
- HTTP: 76 alive / 52 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41580
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
