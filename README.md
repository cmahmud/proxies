# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 473
- HTTP: 138 alive / 97 gold
- HTTPS: 114 alive / 42 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 200 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44915
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
