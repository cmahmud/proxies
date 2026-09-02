# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 451
- HTTP: 104 alive / 76 gold
- HTTPS: 115 alive / 31 gold
- SOCKS4: 182 alive / 165 gold
- SOCKS5: 188 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47435
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
