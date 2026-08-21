# SyndProxy private pool

## Current pool

- Alive now: 1001
- Gold now: 361
- HTTP: 321 alive / 82 gold
- HTTPS: 256 alive / 21 gold
- SOCKS4: 217 alive / 123 gold
- SOCKS5: 207 alive / 135 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29806
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
