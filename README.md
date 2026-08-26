# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 407
- HTTP: 131 alive / 73 gold
- HTTPS: 171 alive / 19 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40385
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
