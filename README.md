# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 418
- HTTP: 339 alive / 93 gold
- HTTPS: 222 alive / 24 gold
- SOCKS4: 228 alive / 151 gold
- SOCKS5: 242 alive / 150 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25170
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
