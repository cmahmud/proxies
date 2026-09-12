# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 462
- HTTP: 125 alive / 94 gold
- HTTPS: 51 alive / 29 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 195 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49418
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
