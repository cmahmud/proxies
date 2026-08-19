# SyndProxy private pool

## Current pool

- Alive now: 1272
- Gold now: 409
- HTTP: 438 alive / 81 gold
- HTTPS: 277 alive / 15 gold
- SOCKS4: 289 alive / 149 gold
- SOCKS5: 268 alive / 164 gold

## Historical pool

- Discovered: 131116
- Ever alive: 20662
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
