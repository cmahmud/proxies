# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 405
- HTTP: 100 alive / 65 gold
- HTTPS: 178 alive / 17 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 190 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41058
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
