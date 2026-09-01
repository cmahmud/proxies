# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 416
- HTTP: 84 alive / 60 gold
- HTTPS: 41 alive / 22 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
