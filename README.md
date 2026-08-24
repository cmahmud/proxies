# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 389
- HTTP: 93 alive / 59 gold
- HTTPS: 39 alive / 12 gold
- SOCKS4: 184 alive / 156 gold
- SOCKS5: 191 alive / 162 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33340
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
