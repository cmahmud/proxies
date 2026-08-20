# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 398
- HTTP: 350 alive / 88 gold
- HTTPS: 252 alive / 23 gold
- SOCKS4: 203 alive / 133 gold
- SOCKS5: 247 alive / 154 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24976
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
