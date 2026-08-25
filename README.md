# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 395
- HTTP: 75 alive / 51 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36561
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
