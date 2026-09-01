# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 409
- HTTP: 78 alive / 62 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 174 alive / 164 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47077
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
