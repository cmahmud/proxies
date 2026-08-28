# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 430
- HTTP: 120 alive / 80 gold
- HTTPS: 127 alive / 22 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42385
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
