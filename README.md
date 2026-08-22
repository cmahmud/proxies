# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 393
- HTTP: 252 alive / 89 gold
- HTTPS: 191 alive / 26 gold
- SOCKS4: 216 alive / 143 gold
- SOCKS5: 237 alive / 135 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31792
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
