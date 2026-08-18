# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 246
- HTTP: 418 alive / 24 gold
- HTTPS: 228 alive / 10 gold
- SOCKS4: 195 alive / 124 gold
- SOCKS5: 191 alive / 88 gold

## Historical pool

- Discovered: 94370
- Ever alive: 10105
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
