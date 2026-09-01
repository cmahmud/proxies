# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 407
- HTTP: 80 alive / 59 gold
- HTTPS: 48 alive / 20 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47080
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
