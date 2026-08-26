# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 396
- HTTP: 127 alive / 74 gold
- HTTPS: 165 alive / 20 gold
- SOCKS4: 162 alive / 148 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40133
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
