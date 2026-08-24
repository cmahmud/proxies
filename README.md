# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 396
- HTTP: 94 alive / 61 gold
- HTTPS: 58 alive / 15 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 174 alive / 161 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33505
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
