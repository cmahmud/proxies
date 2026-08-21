# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 421
- HTTP: 316 alive / 84 gold
- HTTPS: 235 alive / 28 gold
- SOCKS4: 228 alive / 146 gold
- SOCKS5: 256 alive / 163 gold

## Historical pool

- Discovered: 158927
- Ever alive: 30149
- Ever gold: 1142

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
