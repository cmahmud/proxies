# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 390
- HTTP: 133 alive / 72 gold
- HTTPS: 165 alive / 23 gold
- SOCKS4: 158 alive / 144 gold
- SOCKS5: 179 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40004
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
