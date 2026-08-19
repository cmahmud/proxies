# SyndProxy private pool

## Current pool

- Alive now: 1288
- Gold now: 391
- HTTP: 446 alive / 86 gold
- HTTPS: 315 alive / 13 gold
- SOCKS4: 243 alive / 128 gold
- SOCKS5: 284 alive / 164 gold

## Historical pool

- Discovered: 133919
- Ever alive: 21426
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
