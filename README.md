# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 416
- HTTP: 102 alive / 68 gold
- HTTPS: 185 alive / 22 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40624
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
