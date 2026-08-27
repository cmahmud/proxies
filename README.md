# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 412
- HTTP: 99 alive / 65 gold
- HTTPS: 152 alive / 18 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 200 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41097
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
