# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 398
- HTTP: 96 alive / 60 gold
- HTTPS: 161 alive / 15 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 195 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41093
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
