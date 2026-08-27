# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 405
- HTTP: 119 alive / 60 gold
- HTTPS: 157 alive / 12 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40861
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
