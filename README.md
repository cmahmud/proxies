# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 394
- HTTP: 128 alive / 70 gold
- HTTPS: 156 alive / 21 gold
- SOCKS4: 167 alive / 148 gold
- SOCKS5: 182 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40138
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
