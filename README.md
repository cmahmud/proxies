# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 394
- HTTP: 144 alive / 68 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 180 alive / 154 gold
- SOCKS5: 196 alive / 158 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33289
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
