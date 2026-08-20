# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 385
- HTTP: 228 alive / 79 gold
- HTTPS: 146 alive / 19 gold
- SOCKS4: 204 alive / 143 gold
- SOCKS5: 203 alive / 144 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25234
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
