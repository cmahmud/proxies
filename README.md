# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 456
- HTTP: 133 alive / 85 gold
- HTTPS: 127 alive / 36 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 198 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46830
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
