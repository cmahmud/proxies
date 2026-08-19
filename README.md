# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 334
- HTTP: 318 alive / 56 gold
- HTTPS: 199 alive / 13 gold
- SOCKS4: 208 alive / 133 gold
- SOCKS5: 196 alive / 132 gold

## Historical pool

- Discovered: 129233
- Ever alive: 20034
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
