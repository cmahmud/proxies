# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 405
- HTTP: 98 alive / 57 gold
- HTTPS: 159 alive / 15 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40773
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
