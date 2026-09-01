# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 461
- HTTP: 126 alive / 86 gold
- HTTPS: 128 alive / 36 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 192 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46803
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
