# SyndProxy private pool

## Current pool

- Alive now: 1167
- Gold now: 568
- HTTP: 422 alive / 191 gold
- HTTPS: 284 alive / 95 gold
- SOCKS4: 233 alive / 148 gold
- SOCKS5: 228 alive / 134 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22854
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
