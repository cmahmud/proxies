# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 376
- HTTP: 202 alive / 62 gold
- HTTPS: 121 alive / 17 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 207 alive / 153 gold

## Historical pool

- Discovered: 146656
- Ever alive: 25692
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
