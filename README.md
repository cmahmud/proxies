# SyndProxy private pool

## Current pool

- Alive now: 714
- Gold now: 374
- HTTP: 182 alive / 73 gold
- HTTPS: 128 alive / 17 gold
- SOCKS4: 207 alive / 148 gold
- SOCKS5: 197 alive / 136 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26213
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
