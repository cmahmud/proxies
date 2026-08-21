# SyndProxy private pool

## Current pool

- Alive now: 1126
- Gold now: 449
- HTTP: 366 alive / 99 gold
- HTTPS: 256 alive / 32 gold
- SOCKS4: 250 alive / 163 gold
- SOCKS5: 254 alive / 155 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30261
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
