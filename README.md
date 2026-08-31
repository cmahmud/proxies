# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 484
- HTTP: 142 alive / 101 gold
- HTTPS: 122 alive / 47 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 206 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45011
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
