# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 410
- HTTP: 107 alive / 63 gold
- HTTPS: 162 alive / 18 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41102
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
