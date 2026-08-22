# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 389
- HTTP: 258 alive / 92 gold
- HTTPS: 176 alive / 28 gold
- SOCKS4: 218 alive / 140 gold
- SOCKS5: 213 alive / 129 gold

## Historical pool

- Discovered: 163257
- Ever alive: 31773
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
