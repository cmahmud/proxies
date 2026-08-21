# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 413
- HTTP: 271 alive / 84 gold
- HTTPS: 183 alive / 24 gold
- SOCKS4: 197 alive / 151 gold
- SOCKS5: 243 alive / 154 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28917
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
