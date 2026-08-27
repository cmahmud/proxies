# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 409
- HTTP: 101 alive / 66 gold
- HTTPS: 179 alive / 17 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41065
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
