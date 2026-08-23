# SyndProxy validated proxy pool

## Current pool

- Alive now: 354
- Gold now: 203
- HTTP: 105 alive / 44 gold
- HTTPS: 57 alive / 5 gold
- SOCKS4: 71 alive / 68 gold
- SOCKS5: 121 alive / 86 gold

## Historical pool

- Discovered: 169854
- Ever alive: 32712
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
