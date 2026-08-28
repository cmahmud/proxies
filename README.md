# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 432
- HTTP: 121 alive / 87 gold
- HTTPS: 132 alive / 19 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 196 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42216
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
