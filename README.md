# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 386
- HTTP: 118 alive / 63 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 170 alive / 154 gold
- SOCKS5: 180 alive / 153 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33257
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
