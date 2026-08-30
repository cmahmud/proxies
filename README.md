# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 446
- HTTP: 103 alive / 84 gold
- HTTPS: 55 alive / 29 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43682
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
