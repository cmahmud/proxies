# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 540
- HTTP: 373 alive / 162 gold
- HTTPS: 278 alive / 91 gold
- SOCKS4: 216 alive / 139 gold
- SOCKS5: 236 alive / 148 gold

## Historical pool

- Discovered: 122371
- Ever alive: 18552
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
