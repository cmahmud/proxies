# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 433
- HTTP: 113 alive / 81 gold
- HTTPS: 136 alive / 22 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42354
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
