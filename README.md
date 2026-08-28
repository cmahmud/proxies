# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 405
- HTTP: 80 alive / 60 gold
- HTTPS: 97 alive / 21 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42980
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
