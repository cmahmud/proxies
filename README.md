# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 418
- HTTP: 100 alive / 77 gold
- HTTPS: 121 alive / 23 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 185 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41850
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
