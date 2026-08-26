# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 390
- HTTP: 127 alive / 70 gold
- HTTPS: 155 alive / 18 gold
- SOCKS4: 167 alive / 148 gold
- SOCKS5: 182 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40138
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
