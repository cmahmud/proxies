# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 419
- HTTP: 98 alive / 67 gold
- HTTPS: 51 alive / 23 gold
- SOCKS4: 181 alive / 166 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49018
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
