# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 396
- HTTP: 83 alive / 65 gold
- HTTPS: 83 alive / 14 gold
- SOCKS4: 158 alive / 153 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43225
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
