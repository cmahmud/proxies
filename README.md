# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 399
- HTTP: 126 alive / 73 gold
- HTTPS: 161 alive / 18 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 181 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40194
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
