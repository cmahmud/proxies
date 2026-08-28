# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 433
- HTTP: 110 alive / 79 gold
- HTTPS: 133 alive / 24 gold
- SOCKS4: 182 alive / 160 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42351
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
