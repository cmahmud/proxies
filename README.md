# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 392
- HTTP: 261 alive / 93 gold
- HTTPS: 162 alive / 27 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 223 alive / 131 gold

## Historical pool

- Discovered: 163259
- Ever alive: 31777
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
