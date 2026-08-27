# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 392
- HTTP: 79 alive / 54 gold
- HTTPS: 56 alive / 13 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41580
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
