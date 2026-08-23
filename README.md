# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 361
- HTTP: 111 alive / 36 gold
- HTTPS: 48 alive / 10 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 189 alive / 156 gold

## Historical pool

- Discovered: 171584
- Ever alive: 32927
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
