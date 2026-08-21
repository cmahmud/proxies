# SyndProxy private pool

## Current pool

- Alive now: 824
- Gold now: 418
- HTTP: 228 alive / 86 gold
- HTTPS: 118 alive / 21 gold
- SOCKS4: 235 alive / 154 gold
- SOCKS5: 243 alive / 157 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29748
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
