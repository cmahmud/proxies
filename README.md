# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 414
- HTTP: 98 alive / 74 gold
- HTTPS: 103 alive / 18 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42055
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
