# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 396
- HTTP: 93 alive / 61 gold
- HTTPS: 57 alive / 15 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33505
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
