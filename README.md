# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 420
- HTTP: 117 alive / 73 gold
- HTTPS: 81 alive / 18 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37988
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
