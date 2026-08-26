# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 377
- HTTP: 127 alive / 70 gold
- HTTPS: 174 alive / 16 gold
- SOCKS4: 161 alive / 145 gold
- SOCKS5: 171 alive / 146 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39916
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
