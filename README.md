# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 396
- HTTP: 91 alive / 60 gold
- HTTPS: 56 alive / 15 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33505
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
