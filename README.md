# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 376
- HTTP: 88 alive / 56 gold
- HTTPS: 54 alive / 9 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 182 alive / 154 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33093
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
