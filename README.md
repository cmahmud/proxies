# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 411
- HTTP: 119 alive / 65 gold
- HTTPS: 163 alive / 17 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40801
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
