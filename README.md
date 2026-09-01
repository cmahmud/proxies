# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 424
- HTTP: 83 alive / 67 gold
- HTTPS: 91 alive / 30 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47315
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
