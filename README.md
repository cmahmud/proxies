# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 412
- HTTP: 103 alive / 66 gold
- HTTPS: 189 alive / 15 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40696
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
