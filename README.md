# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 385
- HTTP: 172 alive / 83 gold
- HTTPS: 122 alive / 19 gold
- SOCKS4: 219 alive / 134 gold
- SOCKS5: 228 alive / 149 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29762
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
