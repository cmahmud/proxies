# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 424
- HTTP: 121 alive / 75 gold
- HTTPS: 162 alive / 24 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40496
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
