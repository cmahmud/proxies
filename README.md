# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 345
- HTTP: 104 alive / 37 gold
- HTTPS: 46 alive / 10 gold
- SOCKS4: 177 alive / 154 gold
- SOCKS5: 174 alive / 144 gold

## Historical pool

- Discovered: 171048
- Ever alive: 32856
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
