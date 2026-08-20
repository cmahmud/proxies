# SyndProxy private pool

## Current pool

- Alive now: 1503
- Gold now: 633
- HTTP: 565 alive / 234 gold
- HTTPS: 473 alive / 119 gold
- SOCKS4: 206 alive / 136 gold
- SOCKS5: 259 alive / 144 gold

## Historical pool

- Discovered: 142729
- Ever alive: 24578
- Ever gold: 1028

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
