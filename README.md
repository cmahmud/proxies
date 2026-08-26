# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 404
- HTTP: 147 alive / 72 gold
- HTTPS: 160 alive / 19 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 186 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40350
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
