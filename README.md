# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 413
- HTTP: 270 alive / 82 gold
- HTTPS: 241 alive / 26 gold
- SOCKS4: 198 alive / 134 gold
- SOCKS5: 254 alive / 171 gold

## Historical pool

- Discovered: 161927
- Ever alive: 31203
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
