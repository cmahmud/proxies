# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 461
- HTTP: 148 alive / 91 gold
- HTTPS: 122 alive / 36 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46872
- Ever gold: 1453

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
