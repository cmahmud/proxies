# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 390
- HTTP: 238 alive / 76 gold
- HTTPS: 144 alive / 18 gold
- SOCKS4: 216 alive / 149 gold
- SOCKS5: 235 alive / 147 gold

## Historical pool

- Discovered: 156831
- Ever alive: 29632
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
