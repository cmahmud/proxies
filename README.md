# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 405
- HTTP: 103 alive / 68 gold
- HTTPS: 182 alive / 20 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40591
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
