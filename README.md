# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 365
- HTTP: 71 alive / 42 gold
- HTTPS: 37 alive / 8 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 184 alive / 159 gold

## Historical pool

- Discovered: 173056
- Ever alive: 32999
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
