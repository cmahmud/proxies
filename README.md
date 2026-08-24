# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 392
- HTTP: 95 alive / 59 gold
- HTTPS: 49 alive / 15 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33504
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
