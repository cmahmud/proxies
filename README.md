# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 393
- HTTP: 136 alive / 73 gold
- HTTPS: 170 alive / 22 gold
- SOCKS4: 156 alive / 145 gold
- SOCKS5: 174 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40002
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
