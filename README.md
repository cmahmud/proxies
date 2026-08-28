# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 394
- HTTP: 86 alive / 64 gold
- HTTPS: 88 alive / 12 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43229
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
