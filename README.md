# SyndProxy validated proxy pool

## Current pool

- Alive now: 459
- Gold now: 368
- HTTP: 92 alive / 48 gold
- HTTPS: 24 alive / 11 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 173 alive / 156 gold

## Historical pool

- Discovered: 173752
- Ever alive: 33024
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
