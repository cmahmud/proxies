# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 434
- HTTP: 122 alive / 81 gold
- HTTPS: 138 alive / 23 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42349
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
