# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 430
- HTTP: 129 alive / 82 gold
- HTTPS: 148 alive / 19 gold
- SOCKS4: 188 alive / 161 gold
- SOCKS5: 196 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42206
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
