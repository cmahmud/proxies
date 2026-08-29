# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 394
- HTTP: 92 alive / 68 gold
- HTTPS: 86 alive / 16 gold
- SOCKS4: 163 alive / 150 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43262
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
