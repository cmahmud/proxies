# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 421
- HTTP: 91 alive / 67 gold
- HTTPS: 53 alive / 25 gold
- SOCKS4: 187 alive / 167 gold
- SOCKS5: 176 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49037
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
