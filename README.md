# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 394
- HTTP: 240 alive / 88 gold
- HTTPS: 179 alive / 27 gold
- SOCKS4: 212 alive / 144 gold
- SOCKS5: 228 alive / 135 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31794
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
