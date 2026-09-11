# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 396
- HTTP: 98 alive / 65 gold
- HTTPS: 37 alive / 22 gold
- SOCKS4: 154 alive / 139 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48772
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
