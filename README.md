# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 255
- HTTP: 216 alive / 30 gold
- HTTPS: 108 alive / 8 gold
- SOCKS4: 231 alive / 125 gold
- SOCKS5: 226 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9087
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
