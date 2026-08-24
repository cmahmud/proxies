# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 388
- HTTP: 98 alive / 59 gold
- HTTPS: 45 alive / 16 gold
- SOCKS4: 170 alive / 155 gold
- SOCKS5: 178 alive / 158 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33504
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
