# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 405
- HTTP: 111 alive / 66 gold
- HTTPS: 165 alive / 11 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40940
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
