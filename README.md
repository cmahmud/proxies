# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 342
- HTTP: 285 alive / 70 gold
- HTTPS: 207 alive / 17 gold
- SOCKS4: 195 alive / 111 gold
- SOCKS5: 232 alive / 144 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16130
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
