# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 403
- HTTP: 111 alive / 80 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 165 alive / 147 gold
- SOCKS5: 183 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48061
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
