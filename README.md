# SyndProxy validated proxy pool

## Current pool

- Alive now: 385
- Gold now: 316
- HTTP: 90 alive / 62 gold
- HTTPS: 37 alive / 22 gold
- SOCKS4: 116 alive / 103 gold
- SOCKS5: 142 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49512
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
