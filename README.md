# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 438
- HTTP: 372 alive / 104 gold
- HTTPS: 237 alive / 25 gold
- SOCKS4: 204 alive / 144 gold
- SOCKS5: 255 alive / 165 gold

## Historical pool

- Discovered: 152769
- Ever alive: 28402
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
