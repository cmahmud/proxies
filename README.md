# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 384
- HTTP: 111 alive / 53 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33473
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
