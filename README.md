# SyndProxy validated proxy pool

## Current pool

- Alive now: 670
- Gold now: 425
- HTTP: 126 alive / 76 gold
- HTTPS: 183 alive / 25 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40492
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
