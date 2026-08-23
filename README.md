# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 363
- HTTP: 78 alive / 40 gold
- HTTPS: 42 alive / 8 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 197 alive / 159 gold

## Historical pool

- Discovered: 173056
- Ever alive: 32999
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
