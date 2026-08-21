# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 398
- HTTP: 212 alive / 92 gold
- HTTPS: 122 alive / 24 gold
- SOCKS4: 176 alive / 123 gold
- SOCKS5: 230 alive / 159 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29480
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
