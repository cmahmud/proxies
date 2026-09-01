# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 474
- HTTP: 146 alive / 97 gold
- HTTPS: 113 alive / 36 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 197 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46343
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
