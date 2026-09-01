# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 461
- HTTP: 133 alive / 84 gold
- HTTPS: 129 alive / 35 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 196 alive / 181 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46765
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
