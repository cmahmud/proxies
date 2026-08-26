# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 405
- HTTP: 128 alive / 71 gold
- HTTPS: 165 alive / 17 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40425
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
