# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 411
- HTTP: 100 alive / 65 gold
- HTTPS: 99 alive / 18 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42578
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
