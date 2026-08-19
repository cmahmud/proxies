# SyndProxy private pool

## Current pool

- Alive now: 1326
- Gold now: 404
- HTTP: 445 alive / 94 gold
- HTTPS: 365 alive / 16 gold
- SOCKS4: 244 alive / 130 gold
- SOCKS5: 272 alive / 164 gold

## Historical pool

- Discovered: 133349
- Ever alive: 21419
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
