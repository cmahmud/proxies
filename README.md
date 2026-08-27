# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 417
- HTTP: 98 alive / 58 gold
- HTTPS: 94 alive / 23 gold
- SOCKS4: 180 alive / 167 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41538
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
