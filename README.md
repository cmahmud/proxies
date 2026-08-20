# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 376
- HTTP: 209 alive / 76 gold
- HTTPS: 143 alive / 16 gold
- SOCKS4: 209 alive / 144 gold
- SOCKS5: 217 alive / 140 gold

## Historical pool

- Discovered: 148338
- Ever alive: 26309
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
