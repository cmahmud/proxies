# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 434
- HTTP: 120 alive / 85 gold
- HTTPS: 137 alive / 20 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42275
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
