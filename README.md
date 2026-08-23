# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 334
- HTTP: 109 alive / 38 gold
- HTTPS: 62 alive / 9 gold
- SOCKS4: 169 alive / 148 gold
- SOCKS5: 174 alive / 139 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32792
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
