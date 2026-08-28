# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 437
- HTTP: 118 alive / 83 gold
- HTTPS: 137 alive / 24 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42356
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
