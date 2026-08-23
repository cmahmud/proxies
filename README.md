# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 354
- HTTP: 110 alive / 36 gold
- HTTPS: 77 alive / 8 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 198 alive / 156 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32918
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
