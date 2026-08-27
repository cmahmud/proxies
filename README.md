# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 418
- HTTP: 121 alive / 65 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 174 alive / 165 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41275
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
