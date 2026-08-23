# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 338
- HTTP: 111 alive / 41 gold
- HTTPS: 72 alive / 9 gold
- SOCKS4: 169 alive / 149 gold
- SOCKS5: 176 alive / 139 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32792
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
