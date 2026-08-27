# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 410
- HTTP: 103 alive / 67 gold
- HTTPS: 177 alive / 20 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40589
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
