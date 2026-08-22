# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 414
- HTTP: 246 alive / 97 gold
- HTTPS: 166 alive / 32 gold
- SOCKS4: 218 alive / 144 gold
- SOCKS5: 217 alive / 141 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31761
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
