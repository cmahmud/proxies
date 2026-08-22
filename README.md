# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 413
- HTTP: 353 alive / 90 gold
- HTTPS: 237 alive / 37 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 238 alive / 144 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31719
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
