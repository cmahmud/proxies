# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 403
- HTTP: 88 alive / 60 gold
- HTTPS: 79 alive / 18 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39040
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
