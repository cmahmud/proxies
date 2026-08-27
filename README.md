# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 405
- HTTP: 113 alive / 63 gold
- HTTPS: 150 alive / 16 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41251
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
