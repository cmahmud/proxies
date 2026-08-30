# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 449
- HTTP: 108 alive / 84 gold
- HTTPS: 55 alive / 30 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 185 alive / 174 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43681
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
