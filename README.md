# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 408
- HTTP: 77 alive / 58 gold
- HTTPS: 48 alive / 19 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47080
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
