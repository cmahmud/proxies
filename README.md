# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 412
- HTTP: 107 alive / 65 gold
- HTTPS: 155 alive / 17 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 196 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41113
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
