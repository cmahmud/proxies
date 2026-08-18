# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 350
- HTTP: 395 alive / 51 gold
- HTTPS: 219 alive / 13 gold
- SOCKS4: 228 alive / 141 gold
- SOCKS5: 242 alive / 145 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14856
- Ever gold: 475

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
