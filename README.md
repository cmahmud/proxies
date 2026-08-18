# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 254
- HTTP: 212 alive / 30 gold
- HTTPS: 106 alive / 8 gold
- SOCKS4: 230 alive / 124 gold
- SOCKS5: 224 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9087
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
