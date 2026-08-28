# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 442
- HTTP: 126 alive / 87 gold
- HTTPS: 143 alive / 22 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42241
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
