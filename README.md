# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 416
- HTTP: 122 alive / 71 gold
- HTTPS: 175 alive / 20 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40540
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
