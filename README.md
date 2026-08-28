# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 392
- HTTP: 83 alive / 55 gold
- HTTPS: 72 alive / 16 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 176 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42879
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
