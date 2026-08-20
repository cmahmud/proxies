# SyndProxy private pool

## Current pool

- Alive now: 1366
- Gold now: 579
- HTTP: 470 alive / 188 gold
- HTTPS: 334 alive / 99 gold
- SOCKS4: 239 alive / 136 gold
- SOCKS5: 323 alive / 156 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23210
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
