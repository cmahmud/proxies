# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 420
- HTTP: 110 alive / 77 gold
- HTTPS: 123 alive / 19 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42140
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
