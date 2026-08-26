# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 403
- HTTP: 122 alive / 75 gold
- HTTPS: 153 alive / 23 gold
- SOCKS4: 168 alive / 149 gold
- SOCKS5: 186 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40163
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
