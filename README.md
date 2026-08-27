# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 412
- HTTP: 101 alive / 65 gold
- HTTPS: 149 alive / 18 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 198 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41098
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
