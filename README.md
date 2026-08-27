# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 417
- HTTP: 106 alive / 76 gold
- HTTPS: 121 alive / 22 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41852
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
