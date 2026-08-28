# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 427
- HTTP: 115 alive / 80 gold
- HTTPS: 149 alive / 21 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42367
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
