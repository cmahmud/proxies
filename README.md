# SyndProxy private pool

## Current pool

- Alive now: 853
- Gold now: 413
- HTTP: 250 alive / 97 gold
- HTTPS: 174 alive / 32 gold
- SOCKS4: 214 alive / 144 gold
- SOCKS5: 215 alive / 140 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31760
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
