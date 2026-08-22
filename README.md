# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 386
- HTTP: 257 alive / 88 gold
- HTTPS: 206 alive / 25 gold
- SOCKS4: 213 alive / 142 gold
- SOCKS5: 236 alive / 131 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31792
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
