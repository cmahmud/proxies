# SyndProxy validated proxy pool

## Current pool

- Alive now: 340
- Gold now: 209
- HTTP: 114 alive / 45 gold
- HTTPS: 34 alive / 6 gold
- SOCKS4: 85 alive / 67 gold
- SOCKS5: 107 alive / 91 gold

## Historical pool

- Discovered: 170533
- Ever alive: 32760
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
