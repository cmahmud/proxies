# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 433
- HTTP: 113 alive / 81 gold
- HTTPS: 134 alive / 21 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42285
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
