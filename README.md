# SyndProxy validated proxy pool

## Current pool

- Alive now: 352
- Gold now: 197
- HTTP: 105 alive / 45 gold
- HTTPS: 54 alive / 5 gold
- SOCKS4: 71 alive / 64 gold
- SOCKS5: 122 alive / 83 gold

## Historical pool

- Discovered: 169854
- Ever alive: 32712
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
