# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 418
- HTTP: 98 alive / 77 gold
- HTTPS: 126 alive / 16 gold
- SOCKS4: 185 alive / 158 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42148
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
