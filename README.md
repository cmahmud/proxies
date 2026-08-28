# SyndProxy validated proxy pool

## Current pool

- Alive now: 459
- Gold now: 403
- HTTP: 75 alive / 56 gold
- HTTPS: 38 alive / 18 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42856
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
