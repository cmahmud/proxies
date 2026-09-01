# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 414
- HTTP: 81 alive / 60 gold
- HTTPS: 49 alive / 21 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47118
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
