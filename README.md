# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 455
- HTTP: 142 alive / 83 gold
- HTTPS: 125 alive / 36 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 198 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46833
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
