# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 421
- HTTP: 110 alive / 76 gold
- HTTPS: 132 alive / 19 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42413
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
