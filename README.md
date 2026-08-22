# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 386
- HTTP: 249 alive / 89 gold
- HTTPS: 153 alive / 25 gold
- SOCKS4: 213 alive / 140 gold
- SOCKS5: 228 alive / 132 gold

## Historical pool

- Discovered: 163259
- Ever alive: 31777
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
