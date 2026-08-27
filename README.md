# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 406
- HTTP: 91 alive / 61 gold
- HTTPS: 63 alive / 22 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41715
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
