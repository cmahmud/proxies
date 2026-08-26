# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 389
- HTTP: 129 alive / 72 gold
- HTTPS: 159 alive / 17 gold
- SOCKS4: 160 alive / 148 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40134
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
