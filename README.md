# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 519
- HTTP: 392 alive / 146 gold
- HTTPS: 247 alive / 90 gold
- SOCKS4: 228 alive / 148 gold
- SOCKS5: 211 alive / 135 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17717
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
