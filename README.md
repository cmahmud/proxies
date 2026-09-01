# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 424
- HTTP: 86 alive / 64 gold
- HTTPS: 81 alive / 28 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47157
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
