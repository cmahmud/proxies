# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 406
- HTTP: 112 alive / 63 gold
- HTTPS: 163 alive / 14 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41124
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
