# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 435
- HTTP: 331 alive / 87 gold
- HTTPS: 216 alive / 28 gold
- SOCKS4: 228 alive / 159 gold
- SOCKS5: 272 alive / 161 gold

## Historical pool

- Discovered: 164942
- Ever alive: 32197
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
