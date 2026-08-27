# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 417
- HTTP: 95 alive / 66 gold
- HTTPS: 118 alive / 21 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41449
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
