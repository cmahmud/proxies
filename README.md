# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 402
- HTTP: 101 alive / 61 gold
- HTTPS: 168 alive / 17 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41053
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
