# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 337
- HTTP: 108 alive / 38 gold
- HTTPS: 62 alive / 6 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 191 alive / 139 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32894
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
