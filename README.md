# SyndProxy private pool

## Current pool

- Alive now: 792
- Gold now: 405
- HTTP: 222 alive / 94 gold
- HTTPS: 131 alive / 29 gold
- SOCKS4: 209 alive / 144 gold
- SOCKS5: 230 alive / 138 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31798
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
