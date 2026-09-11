# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 418
- HTTP: 98 alive / 66 gold
- HTTPS: 41 alive / 20 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48875
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
