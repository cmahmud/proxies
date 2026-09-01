# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 416
- HTTP: 85 alive / 61 gold
- HTTPS: 71 alive / 20 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47123
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
