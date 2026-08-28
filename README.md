# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 417
- HTTP: 119 alive / 78 gold
- HTTPS: 145 alive / 15 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 190 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42312
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
