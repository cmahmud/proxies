# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 547
- HTTP: 408 alive / 172 gold
- HTTPS: 328 alive / 80 gold
- SOCKS4: 207 alive / 148 gold
- SOCKS5: 205 alive / 147 gold

## Historical pool

- Discovered: 127333
- Ever alive: 19746
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
