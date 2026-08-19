# SyndProxy private pool

## Current pool

- Alive now: 1242
- Gold now: 402
- HTTP: 410 alive / 91 gold
- HTTPS: 307 alive / 20 gold
- SOCKS4: 229 alive / 139 gold
- SOCKS5: 296 alive / 152 gold

## Historical pool

- Discovered: 135761
- Ever alive: 22204
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
