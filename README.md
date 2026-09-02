# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 452
- HTTP: 106 alive / 76 gold
- HTTPS: 112 alive / 32 gold
- SOCKS4: 184 alive / 165 gold
- SOCKS5: 187 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47435
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
