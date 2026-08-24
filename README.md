# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 399
- HTTP: 123 alive / 73 gold
- HTTPS: 60 alive / 15 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 183 alive / 156 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33269
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
