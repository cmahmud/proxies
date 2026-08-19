# SyndProxy private pool

## Current pool

- Alive now: 1287
- Gold now: 386
- HTTP: 433 alive / 92 gold
- HTTPS: 306 alive / 17 gold
- SOCKS4: 268 alive / 137 gold
- SOCKS5: 280 alive / 140 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21565
- Ever gold: 885

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
