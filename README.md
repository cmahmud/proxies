# SyndProxy private pool

## Current pool

- Alive now: 1091
- Gold now: 482
- HTTP: 350 alive / 122 gold
- HTTPS: 243 alive / 72 gold
- SOCKS4: 234 alive / 142 gold
- SOCKS5: 264 alive / 146 gold

## Historical pool

- Discovered: 113576
- Ever alive: 16887
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
