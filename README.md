# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 416
- HTTP: 103 alive / 73 gold
- HTTPS: 81 alive / 22 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 171 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41774
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
