# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 427
- HTTP: 112 alive / 79 gold
- HTTPS: 150 alive / 17 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42326
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
