# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 439
- HTTP: 119 alive / 87 gold
- HTTPS: 59 alive / 27 gold
- SOCKS4: 160 alive / 156 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43661
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
