# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 433
- HTTP: 117 alive / 75 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47598
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
