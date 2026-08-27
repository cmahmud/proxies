# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 406
- HTTP: 90 alive / 60 gold
- HTTPS: 61 alive / 22 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41715
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
