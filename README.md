# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 424
- HTTP: 104 alive / 78 gold
- HTTPS: 126 alive / 22 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 190 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42098
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
