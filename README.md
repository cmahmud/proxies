# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 432
- HTTP: 108 alive / 72 gold
- HTTPS: 64 alive / 27 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45537
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
