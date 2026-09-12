# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 396
- HTTP: 86 alive / 68 gold
- HTTPS: 40 alive / 21 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 178 alive / 152 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49486
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
