# SyndProxy validated proxy pool

## Current pool

- Alive now: 678
- Gold now: 401
- HTTP: 116 alive / 60 gold
- HTTPS: 180 alive / 12 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 203 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40734
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
