# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 357
- HTTP: 286 alive / 87 gold
- HTTPS: 156 alive / 21 gold
- SOCKS4: 190 alive / 119 gold
- SOCKS5: 211 alive / 130 gold

## Historical pool

- Discovered: 167443
- Ever alive: 32586
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
