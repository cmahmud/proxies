# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 417
- HTTP: 84 alive / 62 gold
- HTTPS: 49 alive / 21 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47119
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
