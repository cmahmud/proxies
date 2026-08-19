# SyndProxy private pool

## Current pool

- Alive now: 1218
- Gold now: 460
- HTTP: 460 alive / 122 gold
- HTTPS: 308 alive / 72 gold
- SOCKS4: 226 alive / 138 gold
- SOCKS5: 224 alive / 128 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16717
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
