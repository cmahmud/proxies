# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 455
- HTTP: 116 alive / 87 gold
- HTTPS: 121 alive / 31 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46739
- Ever gold: 1448

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
