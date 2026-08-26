# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 403
- HTTP: 104 alive / 61 gold
- HTTPS: 82 alive / 17 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39071
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
