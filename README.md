# SyndProxy validated proxy pool

## Current pool

- Alive now: 368
- Gold now: 188
- HTTP: 107 alive / 41 gold
- HTTPS: 75 alive / 4 gold
- SOCKS4: 71 alive / 66 gold
- SOCKS5: 115 alive / 77 gold

## Historical pool

- Discovered: 169862
- Ever alive: 32713
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
