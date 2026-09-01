# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 452
- HTTP: 99 alive / 77 gold
- HTTPS: 115 alive / 32 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 190 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47416
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
