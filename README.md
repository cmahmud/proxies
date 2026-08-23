# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 364
- HTTP: 80 alive / 42 gold
- HTTPS: 43 alive / 7 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 202 alive / 159 gold

## Historical pool

- Discovered: 173056
- Ever alive: 32999
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
