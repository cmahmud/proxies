# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 462
- HTTP: 137 alive / 90 gold
- HTTPS: 114 alive / 33 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 206 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46301
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
