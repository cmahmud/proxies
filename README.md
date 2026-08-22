# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 408
- HTTP: 375 alive / 95 gold
- HTTPS: 237 alive / 30 gold
- SOCKS4: 210 alive / 139 gold
- SOCKS5: 226 alive / 144 gold

## Historical pool

- Discovered: 163252
- Ever alive: 31749
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
