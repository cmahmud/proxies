# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 408
- HTTP: 102 alive / 64 gold
- HTTPS: 187 alive / 16 gold
- SOCKS4: 181 alive / 158 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40687
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
