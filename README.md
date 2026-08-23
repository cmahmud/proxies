# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 354
- HTTP: 111 alive / 36 gold
- HTTPS: 66 alive / 8 gold
- SOCKS4: 170 alive / 154 gold
- SOCKS5: 201 alive / 156 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32918
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
