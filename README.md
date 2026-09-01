# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 424
- HTTP: 92 alive / 69 gold
- HTTPS: 93 alive / 30 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47265
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
