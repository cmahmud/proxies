# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 372
- HTTP: 339 alive / 98 gold
- HTTPS: 242 alive / 24 gold
- SOCKS4: 183 alive / 117 gold
- SOCKS5: 228 alive / 133 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28821
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
