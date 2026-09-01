# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 426
- HTTP: 101 alive / 69 gold
- HTTPS: 70 alive / 27 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47044
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
