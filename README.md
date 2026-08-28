# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 445
- HTTP: 131 alive / 87 gold
- HTTPS: 138 alive / 24 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42235
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
