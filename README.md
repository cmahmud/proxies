# SyndProxy private pool

## Current pool

- Alive now: 1142
- Gold now: 534
- HTTP: 424 alive / 160 gold
- HTTPS: 279 alive / 91 gold
- SOCKS4: 206 alive / 139 gold
- SOCKS5: 233 alive / 144 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18625
- Ever gold: 722

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
