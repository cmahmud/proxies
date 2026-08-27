# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 404
- HTTP: 114 alive / 60 gold
- HTTPS: 179 alive / 13 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 203 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40734
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
