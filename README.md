# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 526
- HTTP: 354 alive / 151 gold
- HTTPS: 235 alive / 89 gold
- SOCKS4: 228 alive / 150 gold
- SOCKS5: 211 alive / 136 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17717
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
