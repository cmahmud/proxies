# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 464
- HTTP: 137 alive / 92 gold
- HTTPS: 114 alive / 33 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 204 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46304
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
