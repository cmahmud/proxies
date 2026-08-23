# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 368
- HTTP: 96 alive / 56 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 182 alive / 150 gold

## Historical pool

- Discovered: 174123
- Ever alive: 33058
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
