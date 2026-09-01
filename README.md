# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 420
- HTTP: 85 alive / 62 gold
- HTTPS: 71 alive / 25 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47124
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
