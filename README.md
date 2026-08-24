# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 389
- HTTP: 116 alive / 56 gold
- HTTPS: 65 alive / 14 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 179921
- Ever alive: 33509
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
