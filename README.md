# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 384
- HTTP: 297 alive / 93 gold
- HTTPS: 177 alive / 28 gold
- SOCKS4: 207 alive / 133 gold
- SOCKS5: 216 alive / 130 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31767
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
