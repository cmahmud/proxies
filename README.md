# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 435
- HTTP: 131 alive / 81 gold
- HTTPS: 69 alive / 23 gold
- SOCKS4: 190 alive / 161 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33958
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
