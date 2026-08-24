# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 388
- HTTP: 146 alive / 55 gold
- HTTPS: 58 alive / 15 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 187 alive / 160 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33594
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
