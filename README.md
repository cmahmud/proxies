# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 399
- HTTP: 156 alive / 68 gold
- HTTPS: 63 alive / 13 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 191 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33305
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
