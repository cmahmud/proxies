# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 424
- HTTP: 118 alive / 76 gold
- HTTPS: 172 alive / 23 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40540
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
