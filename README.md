# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 228
- HTTP: 221 alive / 28 gold
- HTTPS: 115 alive / 8 gold
- SOCKS4: 233 alive / 109 gold
- SOCKS5: 214 alive / 83 gold

## Historical pool

- Discovered: 86774
- Ever alive: 7592
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
