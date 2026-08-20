# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 392
- HTTP: 174 alive / 82 gold
- HTTPS: 207 alive / 23 gold
- SOCKS4: 186 alive / 132 gold
- SOCKS5: 204 alive / 155 gold

## Historical pool

- Discovered: 151055
- Ever alive: 27218
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
